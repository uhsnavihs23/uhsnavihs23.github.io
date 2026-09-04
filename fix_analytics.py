import os

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

analytics_scripts = """
    <!-- Cloudflare Web Analytics -->
    <script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "fd1a57da9b654dedb6076173c64023f2"}'></script>
    <!-- End Cloudflare Web Analytics -->

    <!-- PostHog -->
    <script>
        !function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}p||((p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",p.onerror=function(){p=null},(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r));var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],Object.defineProperty(u,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e}}),Object.defineProperty(u.people,"toString",{configurable:!0,enumerable:!0,writable:!0,value:function(){return u.toString(1)+".people (stub)"}}),o="El Rl Pl Al Ll init iu ru Xl tu au fa eu uu Jl cu fu pu capture getExtension nu Ml yu calculateEventProperties mu register register_once register_for_session unregister unregister_for_session ku Yl bu getFeatureFlag getFeatureFlagPayload getFeatureFlagResult getAllFeatureFlags isFeatureEnabled reloadFeatureFlags updateFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys renderSurvey displaySurvey cancelPendingSurvey canRenderSurvey canRenderSurveyAsync Su identify setPersonProperties unsetPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset xu shutdown setIdentity clearIdentity get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException addExceptionStep captureLog startExceptionAutocapture stopExceptionAutocapture loadToolbar get_property getSessionProperty vu createPersonProfile setInternalOrTestUser wu Dl $l opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing hu debug pa ns getPageViewId captureTraceFeedback captureTraceMetric Vl".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
        posthog.init('phc_B8gV2Qx4AaQHHeSZn98cTnyhBBb6tYrQqkZ5Z4zJQ22K', {
            api_host: 'https://us.i.posthog.com',
            person_profiles: 'identified_only',
        })
    </script>
    <!-- End PostHog -->
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Avoid duplicate injection
    if 'data-cf-beacon=' not in content and 'posthog.init' not in content:
        # Inject right before </head>
        content = content.replace('</head>', analytics_scripts + '\n</head>', 1)
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Analytics scripts injected!")
