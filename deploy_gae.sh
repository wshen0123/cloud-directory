[ -z "$GOOG_SDK" ] &&
  echo "Need to set Google App Engine SDK environment variable \$GOOG_SDK" &&
  exit 1;

$GOOG_SDK/appcfg.py update .
