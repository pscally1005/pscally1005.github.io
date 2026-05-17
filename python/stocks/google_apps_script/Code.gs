/**
 * Web hook for poormanprotein.com /misc/stocks subscribe & unsubscribe.
 *
 * Setup (one time):
 * 1. Copy this file into a new project at https://script.google.com
 * 2. Project Settings → Script properties, add:
 *      GITHUB_REPO          owner/repo   (e.g. pscally1005/pscally1005.github.io)
 *      GITHUB_TOKEN         fine-grained PAT with Contents (read/write) + Actions (read)
 *      WEBHOOK_SECRET       random string (same as GitHub secret MAILING_LIST_WEBHOOK_SECRET)
 *      SITE_RETURN_URL      optional; defaults to https://www.poormanprotein.com/misc/stocks
 * 3. Deploy → New deployment → Web app (new version after code changes)
 * 4. Copy the Web app URL into _config.yml as stocks_mailing_api_url
 * 5. Add MAILING_LIST_WEBHOOK_SECRET to GitHub repo secrets
 */

var DEFAULT_RETURN_URL = 'https://www.poormanprotein.com/misc/stocks';

function doGet(e) {
  return handleRequest_(e.parameter || {});
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
  return handleRequest_(params);
}

function returnUrl_(props) {
  return props.getProperty('SITE_RETURN_URL') || DEFAULT_RETURN_URL;
}

function handleRequest_(params) {
  var action = (params.action || '').toLowerCase();
  var props = PropertiesService.getScriptProperties();
  var home = returnUrl_(props);

  try {
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
        return redirectTo_(home + '?mailing=error&reason=invalid_link');
      }
      dispatch_(props, 'stock_unsubscribe', { token: token });
      return redirectTo_(home + '?mailing=unsubscribed');
    }

    return redirectTo_(home + '?mailing=error&reason=unknown');
  } catch (err) {
    return redirectTo_(
      home + '?mailing=error&reason=' + encodeURIComponent(err.message)
    );
  }
}

function dispatch_(props, eventType, payload) {
  var repo = props.getProperty('GITHUB_REPO');
  var token = props.getProperty('GITHUB_TOKEN');
  var secret = props.getProperty('WEBHOOK_SECRET');

  if (!repo || !token || !secret) {
    throw new Error('Apps Script is missing GITHUB_REPO, GITHUB_TOKEN, or WEBHOOK_SECRET.');
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
    throw new Error('GitHub API returned ' + code + ': ' + response.getContentText());
  }
}

function redirectTo_(url) {
  var safeUrl = String(url).replace(/"/g, '%22');
  var html =
    '<!DOCTYPE html><html><head><meta charset="utf-8">' +
    '<meta http-equiv="refresh" content="0;url=' +
    safeUrl +
    '">' +
    '<script>window.location.replace(' +
    JSON.stringify(url) +
    ');</script>' +
    '</head><body><p>Redirecting…</p></body></html>';
  return HtmlService.createHtmlOutput(html).setXFrameOptionsMode(
    HtmlService.XFrameOptionsMode.ALLOWALL
  );
}
