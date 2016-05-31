



<!DOCTYPE html>
<html lang="en" class=" is-copy-enabled">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-89838813501af0ab77e1b954a224433f83e8f31af4b3a4570c8343b6a972ba1c.css" integrity="sha256-iYOIE1Aa8Kt34blUoiRDP4Po8xr0s6RXDINDtqlyuhw=" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-3aba7706d3e768c6769b5d514688402440a602d2e1041baebe2fbbdf3aac24b8.css" integrity="sha256-Orp3BtPnaMZ2m11RRohAJECmAtLhBBuuvi+73zqsJLg=" media="all" rel="stylesheet" />
    
    
    
    

    <link as="script" href="https://assets-cdn.github.com/assets/frameworks-ea5bbb2a837377ffde53e1099e5909c8df4d36cc5e90c05aeb3694b157df7e4d.js" rel="preload" />
    
    <link as="script" href="https://assets-cdn.github.com/assets/github-391829145dbc07158dde112aa636b7ac8b58f7726527ce710bd56118ae1d2f57.js" rel="preload" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=device-width">
    
    
    <title>molSimplify/inparse.py at master · hjkgrp/molSimplify</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="https://avatars3.githubusercontent.com/u/17905841?v=3&amp;s=400" name="twitter:image:src" /><meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="hjkgrp/molSimplify" name="twitter:title" /><meta content="molSimplify code" name="twitter:description" />
      <meta content="https://avatars3.githubusercontent.com/u/17905841?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="hjkgrp/molSimplify" property="og:title" /><meta content="https://github.com/hjkgrp/molSimplify" property="og:url" /><meta content="molSimplify code" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTMyNzYxODU6ZmM1NWJjZjNmYWE3OTE3Y2Q4ZTRhMzIzNGNjMDk3ZmI6NjdhM2FkYWE0MjI0ZDg5NDFjNWM5ZDJmMTQ4NTQwNjYyOGZlYTM0Y2IxMjllNjA2YjE0MzhhMzkzYTNkNWJhZQ==--50ee99013b733f5742d1ad30bd119f046056def4">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="123F01A7:8522:2494CD5D:574DEE17" name="octolytics-dimension-request_id" /><meta content="13276185" name="octolytics-actor-id" /><meta content="jpjanet" name="octolytics-actor-login" /><meta content="d89d5daff3b2a911b43ef74bb16bd498dd3113ff982901ef90b7df40b4890117" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />



  <meta class="js-ga-set" name="dimension1" content="Logged In">



        <meta name="hostname" content="github.com">
    <meta name="user-login" content="jpjanet">

        <meta name="expected-hostname" content="github.com">
      <meta name="js-proxy-site-detection-payload" content="MGYwNTFhYzRhZjExODI5Y2E2NjE1N2ZhMmYyZTE1MjE1MWJkNGNmYWRlMmY3MzdmZDU0ODU1NDRlMjVhNzdjMHx7InJlbW90ZV9hZGRyZXNzIjoiMTguNjMuMS4xNjciLCJyZXF1ZXN0X2lkIjoiMTIzRjAxQTc6ODUyMjoyNDk0Q0Q1RDo1NzRERUUxNyIsInRpbWVzdGFtcCI6MTQ2NDcyNTAyNH0=">


      <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <meta name="html-safe-nonce" content="34e51378b03b5d68a02fac36baef2fd5a957f70a">
    <meta content="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" name="form-nonce" />

    <meta http-equiv="x-pjax-version" content="1d87bcdad141e7582b7d406efff62654">
    

      
  <meta name="description" content="molSimplify code">
  <meta name="go-import" content="github.com/hjkgrp/molSimplify git https://github.com/hjkgrp/molSimplify.git">

  <meta content="17905841" name="octolytics-dimension-user_id" /><meta content="hjkgrp" name="octolytics-dimension-user_login" /><meta content="54120925" name="octolytics-dimension-repository_id" /><meta content="hjkgrp/molSimplify" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="54120925" name="octolytics-dimension-repository_network_root_id" /><meta content="hjkgrp/molSimplify" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/hjkgrp/molSimplify/commits/master.atom" rel="alternate" title="Recent Commits to molSimplify:master" type="application/atom+xml">


      <link rel="canonical" href="https://github.com/hjkgrp/molSimplify/blob/master/Scripts/inparse.py" data-pjax-transient>
  </head>


  <body class="logged-in   env-production linux vis-public page-blob">
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"></div>
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>

    
    
    



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="28" version="1.1" viewBox="0 0 16 16" width="28"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59 0.4 0.07 0.55-0.17 0.55-0.38 0-0.19-0.01-0.82-0.01-1.49-2.01 0.37-2.53-0.49-2.69-0.94-0.09-0.23-0.48-0.94-0.82-1.13-0.28-0.15-0.68-0.52-0.01-0.53 0.63-0.01 1.08 0.58 1.23 0.82 0.72 1.21 1.87 0.87 2.33 0.66 0.07-0.52 0.28-0.87 0.51-1.07-1.78-0.2-3.64-0.89-3.64-3.95 0-0.87 0.31-1.59 0.82-2.15-0.08-0.2-0.36-1.02 0.08-2.12 0 0 0.67-0.21 2.2 0.82 0.64-0.18 1.32-0.27 2-0.27 0.68 0 1.36 0.09 2 0.27 1.53-1.04 2.2-0.82 2.2-0.82 0.44 1.1 0.16 1.92 0.08 2.12 0.51 0.56 0.82 1.27 0.82 2.15 0 3.07-1.87 3.75-3.65 3.95 0.29 0.25 0.54 0.73 0.54 1.48 0 1.07-0.01 1.93-0.01 2.2 0 0.21 0.15 0.46 0.55 0.38C13.71 14.53 16 11.53 16 8 16 3.58 12.42 0 8 0z"></path></svg>
</a>


        <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/search" class="js-site-search-form" data-scoped-search-url="/hjkgrp/molSimplify/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        tabindex="1"
        autocapitalize="off">
    </label>
</form></div>


      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
    
    <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s js-socket-channel js-notification-indicator" data-channel="notification-changed-v2:13276185" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status "></span>
        <svg aria-hidden="true" class="octicon octicon-bell" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 12v1H0v-1l0.73-0.58c0.77-0.77 0.81-2.55 1.19-4.42 0.77-3.77 4.08-5 4.08-5 0-0.55 0.45-1 1-1s1 0.45 1 1c0 0 3.39 1.23 4.16 5 0.38 1.88 0.42 3.66 1.19 4.42l0.66 0.58z m-7 4c1.11 0 2-0.89 2-2H5c0 1.11 0.89 2 2 2z"></path></svg>
</a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <svg aria-hidden="true" class="octicon octicon-plus left" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"></path></svg>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>

  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="hjkgrp">This organization</span>
  </div>
  <a class="dropdown-item" href="/orgs/hjkgrp/invitations/new" data-ga-click="Header, invite someone">
    Invite someone
  </a>
  <a class="dropdown-item" href="/orgs/hjkgrp/new-team" data-ga-click="Header, create new team">
    New team
  </a>
  <a class="dropdown-item" href="/organizations/hjkgrp/repositories/new" data-ga-click="Header, create new organization repository, icon:repo">
    New repository
  </a>


  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="hjkgrp/molSimplify">This repository</span>
  </div>
    <a class="dropdown-item" href="/hjkgrp/molSimplify/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>
    <a class="dropdown-item" href="/hjkgrp/molSimplify/settings/collaboration" data-ga-click="Header, create new collaborator">
      New collaborator
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-sw js-menu-target" href="/jpjanet"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@jpjanet" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/13276185?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu  dropdown-menu-sw">
        <div class=" dropdown-header header-nav-current-user css-truncate">
            Signed in as <strong class="css-truncate-target">jpjanet</strong>

        </div>


        <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/jpjanet" data-ga-click="Header, go to profile, text:your profile">
            Your profile
          </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
          <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
            Explore
          </a>
          <a class="dropdown-item" href="/integrations" data-ga-click="Header, go to integrations, text:integrations">
            Integrations
          </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>


          <div class="dropdown-divider"></div>

          <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
            Settings
          </a>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="80pRkNA4xbNCI6YHkyqi7NaC98GvcL66g9j42RGXck7gnCyAyHzj6yA8v1ZUTLuUwl3Io8/Fs7V9A58Xzlo9HQ==" /></div>
            <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
              Sign out
            </button>
</form>
      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>


      


    <div id="start-of-content" class="accessibility-aid"></div>

      <div id="js-flash-container">
</div>


    <div role="main" class="main-content">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      
<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">

    

<ul class="pagehead-actions">

  <li>
        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="XbRVHLRfDW/bkagJwD4ozsB5/mkxii4LMZYaojw6VRMM85h+b3+5tdpYuKPeEPGXFeIBAhZsI0W1q7EvDLODKQ==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="54120925" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/hjkgrp/molSimplify/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
              <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6c4.94 0 7.94-6 7.94-6S13 2 8.06 2z m-0.06 10c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4z m2-4c0 1.11-0.89 2-2 2s-2-0.89-2-2 0.89-2 2-2 2 0.89 2 2z"></path></svg>
              Watch
            </span>
          </a>
          <a class="social-count js-social-count" href="/hjkgrp/molSimplify/watchers">
            1
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5L4 13 0 9l1.5-1.5 2.5 2.5 6.5-6.5 1.5 1.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6c4.94 0 7.94-6 7.94-6S13 2 8.06 2z m-0.06 10c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4z m2-4c0 1.11-0.89 2-2 2s-2-0.89-2-2 0.89-2 2-2 2 0.89 2 2z"></path></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5L4 13 0 9l1.5-1.5 2.5 2.5 6.5-6.5 1.5 1.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6c4.94 0 7.94-6 7.94-6S13 2 8.06 2z m-0.06 10c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4z m2-4c0 1.11-0.89 2-2 2s-2-0.89-2-2 0.89-2 2-2 2 0.89 2 2z"></path></svg>
                      Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5L4 13 0 9l1.5-1.5 2.5 2.5 6.5-6.5 1.5 1.5z"></path></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M8 2.81v10.38c0 0.67-0.81 1-1.28 0.53L3 10H1c-0.55 0-1-0.45-1-1V7c0-0.55 0.45-1 1-1h2l3.72-3.72c0.47-0.47 1.28-0.14 1.28 0.53z m7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06 1.97 1.97-1.97 1.97 1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06-1.97-1.97 1.97-1.97z"></path></svg>
                      Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/unstar" class="starred" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="sOUZQKkWXoxgJ+DWe9Yf6yqgCTnD7pkSPqybQFL6MbCGoKRdgreIOd7nNgIYiaiErZBdT9+fS/XvwFFCntaj9Q==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar hjkgrp/molSimplify"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-0.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14l4.33-2.33 4.33 2.33L10.4 9.26 14 6z"></path></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/hjkgrp/molSimplify/stargazers">
          1
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/star" class="unstarred" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="vMDAxjFOlcEupr1TAfGbFAMSEbkID4lzVN/6VA/lRW9dGUClO+f3njSmaAlCZnDiHQ9qM7XOH7M0/n/5kBZymQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star hjkgrp/molSimplify"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 6l-4.9-0.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14l4.33-2.33 4.33 2.33L10.4 9.26 14 6z"></path></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/hjkgrp/molSimplify/stargazers">
          1
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of hjkgrp/molSimplify to your account"
              aria-label="Fork your own copy of hjkgrp/molSimplify to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M8 1c-1.11 0-2 0.89-2 2 0 0.73 0.41 1.38 1 1.72v1.28L5 8 3 6v-1.28c0.59-0.34 1-0.98 1-1.72 0-1.11-0.89-2-2-2S0 1.89 0 3c0 0.73 0.41 1.38 1 1.72v1.78l3 3v1.78c-0.59 0.34-1 0.98-1 1.72 0 1.11 0.89 2 2 2s2-0.89 2-2c0-0.73-0.41-1.38-1-1.72V9.5l3-3V4.72c0.59-0.34 1-0.98 1-1.72 0-1.11-0.89-2-2-2zM2 4.2c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z m3 10c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z m3-10c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z"></path></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/hjkgrp/molSimplify/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" />
            </include-fragment>
          </div>

    <a href="/hjkgrp/molSimplify/network" class="social-count">
      0
    </a>
  </li>
</ul>

    <h1 class="entry-title public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M4 9h-1v-1h1v1z m0-3h-1v1h1v-1z m0-2h-1v1h1v-1z m0-2h-1v1h1v-1z m8-1v12c0 0.55-0.45 1-1 1H6v2l-1.5-1.5-1.5 1.5V14H1c-0.55 0-1-0.45-1-1V1C0 0.45 0.45 0 1 0h10c0.55 0 1 0.45 1 1z m-1 10H1v2h2v-1h3v1h5V11z m0-10H2v9h9V1z"></path></svg>
  <span class="author" itemprop="author"><a href="/hjkgrp" class="url fn" rel="author">hjkgrp</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/hjkgrp/molSimplify" data-pjax="#js-repo-pjax-container">molSimplify</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/hjkgrp/molSimplify" aria-selected="true" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /hjkgrp/molSimplify" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M9.5 3l-1.5 1.5 3.5 3.5L8 11.5l1.5 1.5 4.5-5L9.5 3zM4.5 3L0 8l4.5 5 1.5-1.5L2.5 8l3.5-3.5L4.5 3z"></path></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/hjkgrp/molSimplify/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /hjkgrp/molSimplify/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7S10.14 13.7 7 13.7 1.3 11.14 1.3 8s2.56-5.7 5.7-5.7m0-1.3C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7S10.86 1 7 1z m1 3H6v5h2V4z m0 6H6v2h2V10z"></path></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/hjkgrp/molSimplify/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /hjkgrp/molSimplify/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M11 11.28c0-1.73 0-6.28 0-6.28-0.03-0.78-0.34-1.47-0.94-2.06s-1.28-0.91-2.06-0.94c0 0-1.02 0-1 0V0L4 3l3 3V4h1c0.27 0.02 0.48 0.11 0.69 0.31s0.3 0.42 0.31 0.69v6.28c-0.59 0.34-1 0.98-1 1.72 0 1.11 0.89 2 2 2s2-0.89 2-2c0-0.73-0.41-1.38-1-1.72z m-1 2.92c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2zM4 3c0-1.11-0.89-2-2-2S0 1.89 0 3c0 0.73 0.41 1.38 1 1.72 0 1.55 0 5.56 0 6.56-0.59 0.34-1 0.98-1 1.72 0 1.11 0.89 2 2 2s2-0.89 2-2c0-0.73-0.41-1.38-1-1.72V4.72c0.59-0.34 1-0.98 1-1.72z m-0.8 10c0 0.66-0.55 1.2-1.2 1.2s-1.2-0.55-1.2-1.2 0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2z m-1.2-8.8c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z"></path></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/hjkgrp/molSimplify/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /hjkgrp/molSimplify/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M2 5h4v1H2v-1z m0 3h4v-1H2v1z m0 2h4v-1H2v1z m11-5H9v1h4v-1z m0 2H9v1h4v-1z m0 2H9v1h4v-1z m2-6v9c0 0.55-0.45 1-1 1H8.5l-1 1-1-1H1c-0.55 0-1-0.45-1-1V3c0-0.55 0.45-1 1-1h5.5l1 1 1-1h5.5c0.55 0 1 0.45 1 1z m-8 0.5l-0.5-0.5H1v9h6V3.5z m7-0.5H8.5l-0.5 0.5v8.5h6V3z"></path></svg>
      Wiki
</a>

  <a href="/hjkgrp/molSimplify/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /hjkgrp/molSimplify/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0V10h3.6L4.5 8.2l0.9 5.4L9 8.5l1.6 1.5H14V8H11.5z"></path></svg>
    Pulse
</a>
  <a href="/hjkgrp/molSimplify/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /hjkgrp/molSimplify/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15z m-11-1H3V8h2v5z m4 0H7V3h2v10z m4 0H11V6h2v7z"></path></svg>
    Graphs
</a>
    <a href="/hjkgrp/molSimplify/settings" class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks /hjkgrp/molSimplify/settings">
      <svg aria-hidden="true" class="octicon octicon-gear" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M14 8.77V7.17l-1.94-0.64-0.45-1.09 0.88-1.84-1.13-1.13-1.81 0.91-1.09-0.45-0.69-1.92H6.17l-0.63 1.94-1.11 0.45-1.84-0.88-1.13 1.13 0.91 1.81-0.45 1.09L0 7.23v1.59l1.94 0.64 0.45 1.09-0.88 1.84 1.13 1.13 1.81-0.91 1.09 0.45 0.69 1.92h1.59l0.63-1.94 1.11-0.45 1.84 0.88 1.13-1.13-0.92-1.81 0.47-1.09 1.92-0.69zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"></path></svg>
      Settings
</a>
</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/hjkgrp/molSimplify/blob/86f7f6d4309b89afc1c2fda2612dabf2233f2e28/Scripts/inparse.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:b1019dadf77f7f60616cfbaeaab0d8cd -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    title="master"
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/hjkgrp/molSimplify/blob/JP/Scripts/inparse.py"
               data-name="JP"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5L4 13 0 9l1.5-1.5 2.5 2.5 6.5-6.5 1.5 1.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="JP">
                JP
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/hjkgrp/molSimplify/blob/master/Scripts/inparse.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M12 5L4 13 0 9l1.5-1.5 2.5 2.5 6.5-6.5 1.5 1.5z"></path></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text" title="master">
                master
              </span>
            </a>
        </div>

          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="dlf1hOvdpU6vzzKzjvN51NDoHcJOWeLx5sEuU3MM1Suv85yRe7CqlSFyB6TLIdjrM9eJwRt85hHULrEpEj4uaw==" /></div>
          <svg aria-hidden="true" class="octicon octicon-git-branch select-menu-item-icon" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path d="M10 5c0-1.11-0.89-2-2-2s-2 0.89-2 2c0 0.73 0.41 1.38 1 1.72v0.3c-0.02 0.52-0.23 0.98-0.63 1.38s-0.86 0.61-1.38 0.63c-0.83 0.02-1.48 0.16-2 0.45V4.72c0.59-0.34 1-0.98 1-1.72 0-1.11-0.89-2-2-2S0 1.89 0 3c0 0.73 0.41 1.38 1 1.72v6.56C0.41 11.63 0 12.27 0 13c0 1.11 0.89 2 2 2s2-0.89 2-2c0-0.53-0.2-1-0.53-1.36 0.09-0.06 0.48-0.41 0.59-0.47 0.25-0.11 0.56-0.17 0.94-0.17 1.05-0.05 1.95-0.45 2.75-1.25s1.2-1.98 1.25-3.02h-0.02c0.61-0.36 1.02-1 1.02-1.73zM2 1.8c0.66 0 1.2 0.55 1.2 1.2s-0.55 1.2-1.2 1.2-1.2-0.55-1.2-1.2 0.55-1.2 1.2-1.2z m0 12.41c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z m6-8c-0.66 0-1.2-0.55-1.2-1.2s0.55-1.2 1.2-1.2 1.2 0.55 1.2 1.2-0.55 1.2-1.2 1.2z"></path></svg>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="Scripts/inparse.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/hjkgrp/molSimplify/find/master"
          class="js-pjax-capture-input btn btn-sm"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/hjkgrp/molSimplify"><span>molSimplify</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/hjkgrp/molSimplify/tree/master/Scripts"><span>Scripts</span></a></span><span class="separator">/</span><strong class="final-path">inparse.py</strong>
  </div>
</div>

<include-fragment class="commit-tease" src="/hjkgrp/molSimplify/contributors/master/Scripts/inparse.py">
  <div>
    Fetching contributors&hellip;
  </div>

  <div class="commit-tease-contributors">
    <img alt="" class="loader-loading left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
    <span class="loader-error">Cannot retrieve contributors at this time</span>
  </div>
</include-fragment>
<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="btn-group">
      <a href="/hjkgrp/molSimplify/raw/master/Scripts/inparse.py" class="btn btn-sm " id="raw-url">Raw</a>
        <a href="/hjkgrp/molSimplify/blame/master/Scripts/inparse.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
      <a href="/hjkgrp/molSimplify/commits/master/Scripts/inparse.py" class="btn btn-sm " rel="nofollow">History</a>
    </div>


        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/edit/master/Scripts/inparse.py" class="inline-form js-update-url-with-hash" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="vn+R7Wcg9m/7bKySlmFVZiCT+QkSdp4kMt1hs8CHp+RD/r9CHAILHhZmdPTTbdnoTsEKCCg83WGWPB54rW6vIw==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Edit this file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path d="M0 12v3h3l8-8-3-3L0 12z m3 2H1V12h1v1h1v1z m10.3-9.3l-1.3 1.3-3-3 1.3-1.3c0.39-0.39 1.02-0.39 1.41 0l1.59 1.59c0.39 0.39 0.39 1.02 0 1.41z"></path></svg>
          </button>
</form>        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/hjkgrp/molSimplify/delete/master/Scripts/inparse.py" class="inline-form" data-form-nonce="80a3a6303849fb3beb29a227fc9c4fe4d422bb88" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="0rcjPtUM5cQtEN0kHsBznjMUAlxPz8NsmT/3IgvAYniglHlrVKDHfaLoikzJUX0aHSz7BDPxS+yZN58iwMG9Fg==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M10 2H8c0-0.55-0.45-1-1-1H4c-0.55 0-1 0.45-1 1H1c-0.55 0-1 0.45-1 1v1c0 0.55 0.45 1 1 1v9c0 0.55 0.45 1 1 1h7c0.55 0 1-0.45 1-1V5c0.55 0 1-0.45 1-1v-1c0-0.55-0.45-1-1-1z m-1 12H2V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9z m1-10H1v-1h9v1z"></path></svg>
          </button>
</form>  </div>

  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      580 lines (570 sloc)
      <span class="file-info-divider"></span>
    29.2 KB
  </div>
</div>

  

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Written by Tim Ioannidis for HJK Group</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Dpt of Chemical Engineering, MIT</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c">##############################################################</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## This script processes the input file  #############</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c">##############################################################</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># import std modules</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> glob, os, re, argparse, sys</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> io <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> Classes.globalvars <span class="pl-k">import</span> <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c">######################################################</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## check core/ligands specified  #############</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-c">######################################################</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-c">### checks input for correctness ###</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">checkinput</span>(<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    emsg <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check if core is specified</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> (args.core):</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">            emsg <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>You need to specify at least the core of the structures.<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> emsg</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> emsg</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check if ligands are specified</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> args.lig <span class="pl-k">and</span> <span class="pl-k">not</span> args.rgen:</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> args.gui:</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">from</span> Classes.mWidgets <span class="pl-k">import</span> mQDialogWarn</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">            qqb <span class="pl-k">=</span> mQDialogWarn(<span class="pl-s"><span class="pl-pds">&#39;</span>Warning<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>You specified no ligands. Please use the -lig flag. Core only generation..<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">            qqb.setParent(args.gui.wmain)</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>WARNING: You specified no ligands. Please use the -lig flag. Forced generation..<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> emsg</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## check true or false  ###########</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">checkTrue</span>(<span class="pl-smi">arg</span>):</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>y<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> arg.lower() <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> arg.lower() <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>t<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> arg.lower() <span class="pl-k">or</span> arg<span class="pl-k">==</span><span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########################################</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## check for number  ###########</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########################################</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">is_number</span>(<span class="pl-smi">s</span>):</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">float</span>(s)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">import</span> unicodedata</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        unicodedata.numeric(s)</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> (<span class="pl-c1">TypeError</span>, <span class="pl-c1">ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## consolidate lists  #############</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-c">### consolidate arguments ###</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">cleaninput</span>(<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">    globs <span class="pl-k">=</span> globalvars()</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check ligands</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.lig:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        ligdic <span class="pl-k">=</span> readdict(globs.installdir<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>/Ligands/simple_ligands.dict<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.lig):</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> ss <span class="pl-k">in</span> ligdic.keys():</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">                        ss <span class="pl-k">=</span> ligdic[ss][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> s <span class="pl-k">in</span> ligdic.keys():</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                        s <span class="pl-k">=</span> ligdic[s][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        args.lig <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check sminame</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.sminame:</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.sminame):</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        args.sminame <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check qoption</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.qoption:</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.qoption):</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        args.qoption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check sysoption</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.sysoption:</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.sysoption):</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        args.sysoption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check ctrloption</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.ctrloption:</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.ctrloption):</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        args.ctrloption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check scfoption</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.scfoption:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.scfoption):</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">        args.scfoption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check statoption</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.statoption:</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.statoption):</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        args.statoption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># check remoption</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.remoption:</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        ls <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.remoption):</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(s,<span class="pl-c1">list</span>):</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ss <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">                    ls.append(ss)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                ls.append(s)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        args.remoption <span class="pl-k">=</span> ls</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># convert keepHs to boolean</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.keepHs:</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i,s <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(args.keepHs):</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">            args.keepHs[i]<span class="pl-k">=</span>checkTrue(s)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># convert ff option to abe code</span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> args.ff <span class="pl-k">and</span> args.ffoption:</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">        b <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        a <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        e <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        opts <span class="pl-k">=</span> args.ffoption</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>ba<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> opts[<span class="pl-c1">0</span>].lower():</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">            args.ffoption <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>ba<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">            args.ffoption <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> op <span class="pl-k">in</span> opts:</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">                op <span class="pl-k">=</span> op.strip(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> op[<span class="pl-c1">0</span>].lower()<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">                    args.ffoption <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> op[<span class="pl-c1">0</span>].lower()<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">                    args.ffoption <span class="pl-k">+=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> args.ff:</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        args.ffoption <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>ba<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###################################################</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line"><span class="pl-c">##########  parse command line input  #############</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###################################################</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line"><span class="pl-c">### parses inputfile ###</span></td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">parseCLI</span>(<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    cliargs <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(args)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">    s <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,cliargs.split(<span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    fname <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>CLIinput.inp<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">    f <span class="pl-k">=</span> <span class="pl-c1">open</span>(fname,<span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    f.write(<span class="pl-s"><span class="pl-pds">&#39;</span># molSimplify input file generated from CLI input<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> line <span class="pl-k">in</span> s:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">       f.write(<span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span><span class="pl-k">+</span>line<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">    f.close()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> fname</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line"><span class="pl-c">##########  parse input file  #############</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"><span class="pl-c">###########################################</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"><span class="pl-c">### parses inputfile ###</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">parseinput</span>(<span class="pl-smi">args</span>):</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> line <span class="pl-k">in</span> <span class="pl-c1">open</span>(args.i):</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-lig<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> line <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-core<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> line <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-bind<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">            line <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">0</span>] <span class="pl-c"># remove comments</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">        li <span class="pl-k">=</span> line.strip()</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        li <span class="pl-k">=</span> li.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">        line <span class="pl-k">=</span> line.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> li.startswith(<span class="pl-s"><span class="pl-pds">&quot;</span>#<span class="pl-pds">&quot;</span></span>) <span class="pl-k">and</span> <span class="pl-c1">len</span>(li)<span class="pl-k">&gt;</span><span class="pl-c1">0</span>: <span class="pl-c"># remove comments/empty lines</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">            l <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,re.split(<span class="pl-s"><span class="pl-pds">&#39;</span> |,|<span class="pl-cce">\t</span>|&amp;<span class="pl-pds">&#39;</span></span>,li))</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse general arguments</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-core<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                args.core <span class="pl-k">=</span> [ll <span class="pl-k">for</span> ll <span class="pl-k">in</span> l[<span class="pl-c1">1</span>:]]</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ccatoms<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                args.ccatoms <span class="pl-k">=</span> [<span class="pl-c1">int</span>(ll)<span class="pl-k">-</span><span class="pl-c1">1</span> <span class="pl-k">for</span> ll <span class="pl-k">in</span> l[<span class="pl-c1">1</span>:]]</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-rundir<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                args.rundir <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&quot;</span>#<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">0</span>].strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">                args.rundir <span class="pl-k">=</span> args.rundir.split(<span class="pl-s"><span class="pl-pds">&#39;</span>-rundir<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">                args.rundir <span class="pl-k">=</span> args.rundir.lstrip(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (args.rundir[<span class="pl-k">-</span><span class="pl-c1">1</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">                    args.rundir <span class="pl-k">=</span> args.rundir[:<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-suff<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">                args.suff <span class="pl-k">=</span> l[<span class="pl-c1">1</span>].strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">### parse structure generation arguments ###</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-bind<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,re.split(<span class="pl-s"><span class="pl-pds">&#39;</span> |,|<span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>,line[:<span class="pl-k">-</span><span class="pl-c1">1</span>]))</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"># discard comments</span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ibind,lbind <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(l):</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> lbind<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                        l<span class="pl-k">=</span>l[:ibind]</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                        <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">                args.bind <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-nbind<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">                args.bindnum <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-bcharge<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):  <span class="pl-c"># parse charge for binding species</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">                args.bcharge <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-btheta<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">                args.btheta <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-bphi<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">                args.bphi <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-bsep<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">                args.bsep <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-bref<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">                args.bref <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-nambsmi<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">                args.nambsmi <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-maxd<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">                args.maxd <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-mind<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">                args.mind <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-oxstate<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">                args.oxstate <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-coord<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">                args.coord <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-geometry<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">                args.geometry <span class="pl-k">=</span> l[<span class="pl-c1">1</span>].lower()</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse ligands</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-lig<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">                ll <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>-lig<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">                args.lig <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,re.split(<span class="pl-s"><span class="pl-pds">&#39;</span> |,|<span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>,ll))</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-lignum<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">                args.lignum <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-liggrp<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">                args.liggrp <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ligctg<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">                args.ligctg <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ligocc<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">                args.ligocc <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-rkHs<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">                args.rkHs <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ligloc<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">                args.ligloc <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ligalign<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">                args.ligalign <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-replig<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">                args.replig <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-genall<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                args.genall <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-MLbonds<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">                args.MLbonds <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-distort<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">                args.distort <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-rgen<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                args.rgen <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-keepHs<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">                args.keepHs <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ff<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">                args.ff <span class="pl-k">=</span> l[<span class="pl-c1">1</span>].lower()</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ffoption<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">                args.ffoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-place<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">                args.place <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-sminame<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.sminame:</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">                    args.sminame.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">                    args.sminame <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-smicat<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">                args.smicat <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>smicat<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">1</span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> l.replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> re.split(<span class="pl-s"><span class="pl-pds">&#39;</span>/|<span class="pl-cce">\t</span>|&amp;<span class="pl-pds">&#39;</span></span>,l)</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ll <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                    lloc <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">                    l1 <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,re.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,| <span class="pl-pds">&#39;</span></span>,ll))</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">for</span> lll <span class="pl-k">in</span> l1:</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">                        lloc.append(<span class="pl-c1">int</span>(lll)<span class="pl-k">-</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                    args.smicat.append(lloc)</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-pangles<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line:</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                args.pangles <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> <span class="pl-c1">filter</span>(<span class="pl-c1">None</span>,line.split(<span class="pl-s"><span class="pl-pds">&#39;</span>pangles<span class="pl-pds">&#39;</span></span>,<span class="pl-c1">1</span>)[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> l.replace(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">                l <span class="pl-k">=</span> re.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,|<span class="pl-cce">\t</span>|&amp;|<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>,l)</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ll <span class="pl-k">in</span> l:</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                    args.pangles.append(ll) <span class="pl-k">if</span> ll<span class="pl-k">!=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span> args.pangles.append(<span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse qc arguments</span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-qccode<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                args.qccode <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-calccharge<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">                args.calccharge <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-charge<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">                args.charge <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-spin<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                args.spin <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-runtyp<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">                args.runtyp <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-method<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-c1">len</span>(l[<span class="pl-c1">1</span>:]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">                args.method <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse terachem arguments</span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-basis<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                args.basis <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dispersion<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                args.dispersion <span class="pl-k">=</span> l[<span class="pl-c1">1</span>].strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>).lower()</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-qoption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.qoption:</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">                    args.qoption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">                    args.qoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse qchem arguments</span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-exchange<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">                args.exchange <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-correlation<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">                args.correlation <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-unrestricted<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">                args.unrestricted <span class="pl-k">=</span> checkTrue(l[<span class="pl-c1">1</span>])</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-remoption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.remoption:</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">                    args.remoption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">                    args.remoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse gamess arguments</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-gbasis<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">                args.gbasis <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ngauss<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">                args.ngauss <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-npfunc<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">                args.npfunc <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ndfunc<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">                args.ndfunc <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-sysoption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.sysoption:</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">                    args.sysoption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">                    args.sysoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-ctrloption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.ctrloption:</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">                    args.ctrloption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">                    args.ctrloption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-scfoption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.scfoption:</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">                    args.scfoption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">                    args.scfoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-statoption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> args.statoption:</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">                    args.statoption.append(l[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">                    args.statoption <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse jobscript arguments</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-jsched<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">                args.jsched <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-jname<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">                args.jname <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-memory<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">                args.memory <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-wtime<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">                args.wtime <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-queue<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">                args.queue <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-gpus<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">                args.gpus <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-cpus<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">                args.cpus <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-modules<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">                args.modules <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-joption<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-k">not</span> args.joption:</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">                    args.joption <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">                opts <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ll <span class="pl-k">in</span> l[<span class="pl-c1">1</span>:]:</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                    opts <span class="pl-k">+=</span> ll<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">                args.joption.append(opts)</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-jcommand<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-k">not</span> args.jcommand:</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">                    args.jcommand <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">                opts <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> ll <span class="pl-k">in</span> l[<span class="pl-c1">1</span>:]:</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">                    opts <span class="pl-k">+=</span> ll<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">                args.jcommand.append(opts)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse database arguments</span></td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbsim<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">                args.dbsearch <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">                args.dbsim <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbresults<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">                args.dbresults <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dboutputf<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">                args.dboutputf <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbbase<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">                args.dbbase <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbsmarts<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">                args.dbsearch <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">                args.dbsmarts <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbcatoms<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">                args.dbcatoms <span class="pl-k">=</span> l[<span class="pl-c1">1</span>:]</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbfinger<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">                args.dbfinger <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbatoms<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">                args.dbatoms <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbbonds<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">                args.dbbonds <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbarbonds<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">                args.dbarbonds <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbsbonds<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">                args.dbsbonds <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-dbmw<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">                args.dbmw <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># parse postprocessing arguments</span></td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-postp<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">                args.postp <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-postqc<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">                args.postqc <span class="pl-k">=</span> l[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-postdir<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">                args.postdir <span class="pl-k">=</span> line.split(<span class="pl-s"><span class="pl-pds">&quot;</span>#<span class="pl-pds">&quot;</span></span>)[<span class="pl-c1">0</span>].strip(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">                args.postdir <span class="pl-k">=</span> args.postdir.split(<span class="pl-s"><span class="pl-pds">&#39;</span>-postdir<span class="pl-pds">&#39;</span></span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">                args.postdir <span class="pl-k">=</span> args.postdir.lstrip(<span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pres<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">                args.pres <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pwfninfo<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">                args.pwfninfo <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pcharge<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">                args.pcharge <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pgencubes<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">                args.pgencubes <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-porbinfo<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">                args.porbinfo <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pdeloc<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">                args.pdeloc <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#if (l[0]==&#39;-pdorbs&#39;):</span></td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">            <span class="pl-c">#    args.pdorbs = True</span></td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> (l[<span class="pl-c1">0</span>]<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&#39;</span>-pnbo<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">                args.pnbo <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#############################################################</span></td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line"><span class="pl-c">########## mainly for help and listing options  #############</span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#############################################################</span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line"><span class="pl-c">### parses commandline arguments and prints help information ###</span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">parsecommandline</span>(<span class="pl-smi">parser</span>):</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">    globs <span class="pl-k">=</span> globalvars()</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">    installdir <span class="pl-k">=</span> globs.installdir<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># first variable is the flag, second is the variable in the structure. e.g -i, --infile assigns something to args.infile</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-i<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--i<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>input file<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># top directory options</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-rundir<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--rundir<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>directory for jobs<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-suff<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--suff<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>suffix for jobs folder.<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># structure generation options</span></td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ccatoms<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ccatoms<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>core connection atoms indices, indexing starting from 1<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-coord<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--coord<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>coordination such as 4,5,6<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># coordination e.g. 6 </span></td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-core<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--core<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>core structure with currently available: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>getcores(installdir),<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c">#e.g. ferrocene</span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-bind<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bind<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>binding species with currently available: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>getbinds(installdir),<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c">#e.g. bisulfate, nitrate, perchlorate -&gt; For binding</span></td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-bcharge<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bcharge<span class="pl-pds">&quot;</span></span>,<span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>binding species charge, default 0<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-bphi<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bphi<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>azimuthal angle phi for binding species, default random between 0 and 180<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-bref<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bref<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>reference atoms for placement of extra molecules, default COM (center of mass). e.g. 1,5 or 1-5, Fe, COM<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-bsep<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bsep<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>flag for separating extra molecule in input or xyz file<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-btheta<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--btheta<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>polar angle theta for binding species, default random between 0 and 360<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-geometry<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--geometry<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>geometry such as TBP (trigonal bipyramidal)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># geometry</span></td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-genall<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--genall<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Generate complex both with and without FF opt.<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># geometry</span></td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-lig<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--lig<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>ligand structure name or SMILES with currently available: <span class="pl-pds">&quot;</span></span><span class="pl-k">+</span>getligs(installdir),<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c">#e.g. acetate (in smilesdict)</span></td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ligocc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ligocc<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of corresponding ligands e.g. 2,2,1<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># e.g. 1,2,1</span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-lignum<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--lignum<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of ligand types e.g. 2<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-liggrp<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--liggrp<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>ligand group for random generation<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ligctg<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ligctg<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>ligand category for random generation<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-rkHs<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--rkHs<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>keep Hydrogens for random generation<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ligloc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ligloc<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>force location of ligands in the structure generation yes/True/1 or no/False/0<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ligalign<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ligalign<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>smart alignment of ligands in the structure generation yes/True/1 or no/False/0<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-MLbonds<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--MLbonds<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>custom M-L bond length for corresponding ligand in A e.g. 1.4<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-distort<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--distort<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>randomly distort backbone. Ranges from 0 (no distortion) to 100. e.g. 20<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-langles<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--langles<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>custom angles (polar theta, azimuthal phi) for corresponding ligand in degrees separated by &#39;/&#39; e.g. 20/30,10/20<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pangles<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pangles<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>custom angles (polar theta, azimuthal phi) for corresponding connectino points in degrees separated by &#39;/&#39; e.g. 20/30,10/20<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-nbind<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--bindnum<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of binding species copies for random placement<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c">#different geometric arrangements for calculating binding energy</span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-rgen<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--rgen<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of random generated molecules<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-replig<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--replig<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>flag for replacing ligand at specified connection point<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ff<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ff<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>select force field for FF optimization. Available: MMFF94, UFF, GAFF, Ghemical<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ffoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ffoption<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>select when to perform FF optimization. Options: B(Before),A(After),BA<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-keepHs<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--keepHs<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>force keep hydrogens. By default ligands are stripped one hydrogen in order to connect to the core<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-smicat<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--smicat<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>connecting atoms corresponding to smiles. Indexing starts at 1 which is the default value as well<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-sminame<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--sminame<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>name for smiles species used in the folder naming. e.g. amm<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-nambsmi<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--nambsmi<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>name of SMILES string for binding species e.g. carbonmonoxide<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-maxd<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--maxd<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>maximum distance above cluster size for molecules placement maxdist=size1+size2+maxd<span class="pl-pds">&quot;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-mind<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--mind<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>minimum distance above cluster size for molecules placement mindist=size1+size2+mind<span class="pl-pds">&quot;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-place<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--place<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>place binding species relative to core. Takes either angle (0-360) or ax/s for axial side<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-oxstate<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--oxstate<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>oxidation state of the metal, used for bond lengths<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># quantum chemistry options</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-qccode<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--qccode<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>quantum chemistry code. Choices: TeraChem or GAMESS or QChem<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-charge<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--charge<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>charge for system (default: neutral).<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-calccharge<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--calccharge<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Flag to calculate charge.<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-spin<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--spin<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>spin multiplicity for system (default: singlet) e.g. 1<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-runtyp<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--runtyp<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>run type. Choices: optimization, energy<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-method<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--method<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>electronic structure method. Specify UDFT for unrestricted calculation(default: b3lyp) e.g. ub3lyp<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># terachem arguments</span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-basis<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--basis<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>basis for terachem or qchem job (default: LACVP* or lanl2dz)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dispersion<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dispersion<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>dispersion forces. Default: no e.g. d2,d3<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-qoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--qoption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for TeraChem in syntax keyword value, e.g. maxit 100<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># qchem arguments</span></td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-exchange<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--exchange<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>exchange in qchem job (default b3lyp)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-correlation<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--correlation<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>correlation in qchem job (default none)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-remoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--remoption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for qchem $rem block in syntax keyword value, e.g. INCFOCK 0<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-unrestricted<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--unrestricted<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>unrestricted calculation, values: 0/1 False/True<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># gamess arguments</span></td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-gbasis<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--gbasis<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>GBASIS option in GAMESS e.g. CCT<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ngauss<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ngauss<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>NGAUSS option in GAMESS e.g. N31<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-npfunc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--npfunc<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>NPFUNC option for diffuse functions in GAMESS e.g. 2<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ndfunc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ndfunc<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>NDFUNC option for diffuse functions in GAMESS e.g. 1<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-sysoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--sysoption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for $SYSTEM GAMESS block in syntax keyword value, e.g. MWORDS 20<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-ctrloption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--ctrloption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for $CONTRL GAMESS block in syntax keyword value, e.g. ISPHER 1<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-scfoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--scfoption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for $SCF GAMESS block in syntax keyword value, e.g. DIIS .TRUE.<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-statoption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--statoption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>extra arguments for $STATPT GAMESS block in syntax keyword value, e.g. NSTEP 100<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># jobscript arguments</span></td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-jsched<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--jsched<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>job scheduling system. Choices: SLURM or SGE<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-jname<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--jname<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>jobs main identifier<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-memory<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--memory<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>memory reserved per thread for job file in G(default: 2G)e.g.2<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-wtime<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--wtime<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>wall time requested in hours for queueing system (default: 168hrs) e.g. 8<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-queue<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--queue<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>queue name e.g gpus<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-gpus<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--gpus<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of GPUS (default: 1)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-cpus<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--cpus<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of CPUs (default: 1)<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-modules<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--modules<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>modules to be loaded for the calculation<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-joption<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--joption<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>additional options for jobscript<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-jcommand<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--jcommand<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>additional commands for jobscript<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># database search arguments</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbsim<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbsim<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>SMILES/ligand/file for similarity search<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbcatoms<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbcatoms<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>connection atoms for similarity search<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbresults<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbresults<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>how many results for similary search or screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dboutputf<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dboutputf<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>output file for search results<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbbase<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbbase<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>database for search<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbsmarts<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbsmarts<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>SMARTS string for screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbfinger<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbfinger<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>fingerprint for similarity search<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbatoms<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbatoms<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of atoms to be used in screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbbonds<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbbonds<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of bonds to be used in screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbarbonds<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbarbonds<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Number of aromatic bonds to be used in screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbsbonds<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbsbonds<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>number of single bonds to be used in screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbmw<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbmw<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>molecular weight to be used in screening<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># post-processing arguments</span></td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-postp<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--postp<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>post process results<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-postqc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--postqc<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>quantum chemistry code used. Choices: TeraChem or GAMESS<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-postdir<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--postdir<span class="pl-pds">&quot;</span></span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>directory with results<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) </td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pres<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pres<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>generate calculations summary<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pdeninfo<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pdeninfo<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>calculate average properties for electron density<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pcharge<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pcharge<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>calculate charges<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pgencubes<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pgencubes<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>generate cubefiles<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pwfninfo<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pwfninfo<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>get information about wavefunction<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pdeloc<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pdeloc<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>get delocalization and localization indices<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-porbinfo<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--porbinfo<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>get information about MO<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-pnbo<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--pnbo<span class="pl-pds">&quot;</span></span>,<span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>post process nbo analysis<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#parser.add_argument(&quot;-pdorbs&quot;,&quot;--pdorbs&quot;,help=&quot;get information on metal d orbitals&quot;,action=&quot;store_true&quot;)</span></td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># auxiliary</span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-dbsearch<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--dbsearch<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># flag for db search</span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-checkdirt<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--checkdirt<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># directory removal check flag</span></td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-checkdirb<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--checkdirb<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>) <span class="pl-c"># directory removal check flag 2</span></td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-jid<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--jid<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)           <span class="pl-c"># job id for folders</span></td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">    parser.add_argument(<span class="pl-s"><span class="pl-pds">&quot;</span>-gui<span class="pl-pds">&quot;</span></span>,<span class="pl-s"><span class="pl-pds">&quot;</span>--gui<span class="pl-pds">&quot;</span></span>,<span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>store_true<span class="pl-pds">&quot;</span></span>)           <span class="pl-c"># gui placeholder</span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># calculations summary (terapostp gampost)</span></td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># nbo</span></td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># charges</span></td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># wavefunction - cube files</span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># deloc indices - basin analysis</span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># moldparse</span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">    args<span class="pl-k">=</span>parser.parse_args()</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> args</td>
      </tr>
</table>

  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="hidden">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop"></div>
</div>


    </div>
  </div>

    </div>

        <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59 0.4 0.07 0.55-0.17 0.55-0.38 0-0.19-0.01-0.82-0.01-1.49-2.01 0.37-2.53-0.49-2.69-0.94-0.09-0.23-0.48-0.94-0.82-1.13-0.28-0.15-0.68-0.52-0.01-0.53 0.63-0.01 1.08 0.58 1.23 0.82 0.72 1.21 1.87 0.87 2.33 0.66 0.07-0.52 0.28-0.87 0.51-1.07-1.78-0.2-3.64-0.89-3.64-3.95 0-0.87 0.31-1.59 0.82-2.15-0.08-0.2-0.36-1.02 0.08-2.12 0 0 0.67-0.21 2.2 0.82 0.64-0.18 1.32-0.27 2-0.27 0.68 0 1.36 0.09 2 0.27 1.53-1.04 2.2-0.82 2.2-0.82 0.44 1.1 0.16 1.92 0.08 2.12 0.51 0.56 0.82 1.27 0.82 2.15 0 3.07-1.87 3.75-3.65 3.95 0.29 0.25 0.54 0.73 0.54 1.48 0 1.07-0.01 1.93-0.01 2.2 0 0.21 0.15 0.46 0.55 0.38C13.71 14.53 16 11.53 16 8 16 3.58 12.42 0 8 0z"></path></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2016 <span title="0.11103s from github-fe150-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



    

    <div id="ajax-error-message" class="ajax-error-message flash flash-error">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15.72 12.5l-6.85-11.98C8.69 0.21 8.36 0.02 8 0.02s-0.69 0.19-0.87 0.5l-6.85 11.98c-0.18 0.31-0.18 0.69 0 1C0.47 13.81 0.8 14 1.15 14h13.7c0.36 0 0.69-0.19 0.86-0.5S15.89 12.81 15.72 12.5zM9 12H7V10h2V12zM9 9H7V5h2V9z"></path></svg>
      <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
        <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
      </button>
      Something went wrong with that request. Please try again.
    </div>


      
      <script crossorigin="anonymous" integrity="sha256-6lu7KoNzd//eU+EJnlkJyN9NNsxekMBa6zaUsVfffk0=" src="https://assets-cdn.github.com/assets/frameworks-ea5bbb2a837377ffde53e1099e5909c8df4d36cc5e90c05aeb3694b157df7e4d.js"></script>
      <script async="async" crossorigin="anonymous" integrity="sha256-ORgpFF28BxWN3hEqpja3rItY93JlJ85xC9VhGK4dL1c=" src="https://assets-cdn.github.com/assets/github-391829145dbc07158dde112aa636b7ac8b58f7726527ce710bd56118ae1d2f57.js"></script>
      
      
      
      
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M15.72 12.5l-6.85-11.98C8.69 0.21 8.36 0.02 8 0.02s-0.69 0.19-0.87 0.5l-6.85 11.98c-0.18 0.31-0.18 0.69 0 1C0.47 13.81 0.8 14 1.15 14h13.7c0.36 0 0.69-0.19 0.86-0.5S15.89 12.81 15.72 12.5zM9 12H7V10h2V12zM9 9H7V5h2V9z"></path></svg>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path d="M7.48 8l3.75 3.75-1.48 1.48-3.75-3.75-3.75 3.75-1.48-1.48 3.75-3.75L0.77 4.25l1.48-1.48 3.75 3.75 3.75-3.75 1.48 1.48-3.75 3.75z"></path></svg>
    </button>
  </div>
</div>

  </body>
</html>

