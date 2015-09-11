[ -z "$GOOG_SDK" ] &&
  echo "Need to set Google App Engine SDK environment variable \$GOOG_SDK" &&
  exit 1;

reset
$GOOG_SDK/dev_appserver.py --clear_datastore true .
