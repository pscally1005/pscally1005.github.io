/**
 * Web hook for poormanprotein.com /misc/stocks subscribe & unsubscribe.
 *
 * Setup (one time):
 * 1. Copy this file into a new project at https://script.google.com
 * 2. Project Settings → Script properties, add:
 *      GITHUB_REPO          owner/repo   (e.g. pscally1005/pscally1005.github.io)
 *      GITHUB_TOKEN         fine-grained PAT with Contents (read/write) + Actions (read)
 *      WEBHOOK_SECRET       random string (same as GitHub secret MAILING_LIST_WEBHOOK_SECRET)
 * 3. Deploy → New deployment → Web app
 *      Execute as: Me
 *      Who has access: Anyone
 * 4. Copy the Web app URL into _config.yml as stocks_mailing_api_url
 * 5. Add MAILING_LIST_WEBHOOK_SECRET to GitHub repo secrets
 */

var SITE_HOME = 'https://www.poormanprotein.com/misc/stocks';

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

function handleRequest_(params) {
  var action = (params.action || '').toLowerCase();
  var props = PropertiesService.getScriptProperties();

  try {
    if (action === 'subscribe') {
      var email = (params.email || '').trim();
      if (!email) {
        return htmlPage_('Missing email address.', false);
      }
      dispatch_(props, 'stock_subscribe', { email: email });
      return htmlPage_(
        'You are subscribed! You will receive the weekday 7 AM Eastern stock report at <strong>' +
          escapeHtml_(email) +
          '</strong>.',
        true
      );
    }

    if (action === 'unsubscribe') {
      var token = (params.token || '').trim();
      if (!token) {
        return htmlPage_('Invalid unsubscribe link.', false);
      }
      dispatch_(props, 'stock_unsubscribe', { token: token });
      return htmlPage_('You have been unsubscribed.', true);
    }

    return htmlPage_('Unknown action.', false);
  } catch (err) {
    return htmlPage_('Error: ' + err.message, false);
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

function htmlPage_(message, success) {
  var color = success ? '#1a7f37' : '#b42318';
  var html =
    '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Stock report mailing list</title>' +
    '<style>body{font-family:sans-serif;max-width:32rem;margin:3rem auto;padding:0 1rem;color:#222}' +
    'a{color:#0969da}</style></head><body>' +
    '<p style="color:' +
    color +
    '">' +
    message +
    '</p>' +
    '<p><a href="' +
    SITE_HOME +
    '">Back to Poor Man Protein</a></p></body></html>';
  return HtmlService.createHtmlOutput(html).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function escapeHtml_(text) {
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
