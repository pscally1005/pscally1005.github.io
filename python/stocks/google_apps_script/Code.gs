/**
 * Web hook for poormanprotein.com /misc/stocks subscribe & unsubscribe.
 *
 * After code changes: Deploy → Manage deployments → Edit → New version → Deploy
 */

var DEFAULT_RETURN_URL = 'https://www.poormanprotein.com/misc/stocks';

function doGet(e) {
  try {
    var params = e.parameter || {};
    var action = (params.action || '').toLowerCase();

    // GET is allowed for subscribing because the subscription form uses it.
    // GET must NOT actually unsubscribe, because email security scanners
    // commonly follow links automatically.
    if (action === 'unsubscribe') {
      var token = (params.token || '').trim();

      if (!token) {
        return donePage_(
          'Invalid unsubscribe link.',
          false,
          DEFAULT_RETURN_URL
        );
      }

      // A GET request only displays a confirmation page.
      return unsubscribeConfirmPage_(token);
    }

    return handleRequest_(params);
  } catch (err) {
    return donePage_(
      'Error: ' + err.message,
      false,
      DEFAULT_RETURN_URL
    );
  }
}

function doPost(e) {
  var params = {};

  if (e.postData && e.postData.contents) {
    try {
      params = JSON.parse(e.postData.contents);
    } catch (err) {
      params = e.parameter || {};
    }
  } else {
    params = e.parameter || {};
  }

  try {
    return handleRequest_(params);
  } catch (err) {
    return donePage_(
      'Error: ' + err.message,
      false,
      DEFAULT_RETURN_URL
    );
  }
}

function returnUrl_(props) {
  return props.getProperty('SITE_RETURN_URL') || DEFAULT_RETURN_URL;
}

function handleRequest_(params) {
  var action = (params.action || '').toLowerCase();
  var props = PropertiesService.getScriptProperties();
  var home = returnUrl_(props);

  if (action === 'subscribe') {
    var email = (params.email || '').trim();

    if (!email) {
      return redirectTo_(home + '?mailing=error&reason=missing_email');
    }

    dispatch_(props, 'stock_subscribe', { email: email });

    return redirectTo_(home + '?mailing=subscribed');
  }

  if (action === 'unsubscribe') {
    var token = (params.token || '').trim();

    if (!token) {
      return donePage_(
        'Invalid unsubscribe link.',
        false,
        DEFAULT_RETURN_URL
      );
    }

    console.log(
      'UNSUBSCRIBE REQUEST',
      new Date().toISOString(),
      token
    );

    dispatch_(props, 'stock_unsubscribe', { token: token });

    return redirectTo_(home + '?mailing=unsubscribed');
  }

  return donePage_('Unknown request.', false, home);
}

function unsubscribeConfirmPage_(token) {
  var safeToken = escapeHtml_(token);

  var html =
    '<!DOCTYPE html>' +
    '<html><head>' +
    '<meta charset="utf-8">' +
    '<base target="_top">' +
    '<title>Unsubscribe — Stock Report</title>' +
    '<style>' +
    'body{font-family:sans-serif;max-width:32rem;margin:3rem auto;padding:0 1rem;color:#222}' +
    'button{padding:.6rem 1.25rem;font-size:1rem;cursor:pointer}' +
    'a{color:#0969da}' +
    '</style>' +
    '</head><body>' +

    '<h2>Unsubscribe from the Stock Report</h2>' +

    '<p>Are you sure you want to unsubscribe from the weekday stock report?</p>' +

    '<form method="post">' +
    '<input type="hidden" name="action" value="unsubscribe">' +
    '<input type="hidden" name="token" value="' + safeToken + '">' +
    '<button type="submit">Yes, unsubscribe me</button>' +
    '</form>' +

    '<p style="margin-top:1.5rem">' +
    '<a href="' + escapeHtml_(DEFAULT_RETURN_URL) + '">' +
    'Cancel</a></p>' +

    '</body></html>';

  return HtmlService.createHtmlOutput(html)
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function dispatch_(props, eventType, payload) {
  var repo = props.getProperty('GITHUB_REPO');
  var token = props.getProperty('GITHUB_TOKEN');
  var secret = props.getProperty('WEBHOOK_SECRET');

  if (!repo || !token || !secret) {
    throw new Error(
      'Apps Script is missing GITHUB_REPO, GITHUB_TOKEN, or WEBHOOK_SECRET.'
    );
  }

  payload.secret = secret;

  var response = UrlFetchApp.fetch(
    'https://api.github.com/repos/' + repo + '/dispatches',
    {
      method: 'post',
      contentType: 'application/json',
      headers: {
        Authorization: 'Bearer ' + token,
        Accept: 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
      },
      payload: JSON.stringify({
        event_type: eventType,
        client_payload: payload,
      }),
      muteHttpExceptions: true,
    }
  );

  var code = response.getResponseCode();

  if (code < 200 || code >= 300) {
    throw new Error(
      'GitHub API returned ' +
      code +
      ': ' +
      response.getContentText()
    );
  }
}

function redirectTo_(url) {
  return donePage_('Done. Redirecting…', true, url);
}

function donePage_(message, success, continueUrl) {
  var color = success ? '#1a7f37' : '#b42318';
  var safeUrl = escapeHtml_(continueUrl);

  var html =
    '<!DOCTYPE html><html><head><meta charset="utf-8">' +
    '<base target="_top">' +
    '<title>Stock report mailing list</title>' +
    '<style>' +
    'body{font-family:sans-serif;max-width:32rem;margin:3rem auto;padding:0 1rem;color:#222}' +
    'a{color:#0969da}' +
    '</style>' +
    '<meta http-equiv="refresh" content="2;url=' +
    safeUrl +
    '">' +
    '</head><body>' +

    '<p style="color:' +
    color +
    '">' +
    escapeHtml_(message) +
    '</p>' +

    '<p><a href="' +
    safeUrl +
    '">Continue to Poor Man Protein</a></p>' +

    '<script>' +
    'setTimeout(function(){window.top.location.href=' +
    JSON.stringify(continueUrl) +
    '},500);' +
    '</script>' +

    '</body></html>';

  return HtmlService.createHtmlOutput(html)
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function escapeHtml_(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
