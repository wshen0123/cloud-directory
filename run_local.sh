[ -z "$GOOG_SDK" ] &&
  echo "Need to set Google App Engine SDK environment variable \$GOOG_SDK" &&
  exit 1;

reset
$GOOG_SDK/dev_appserver.py --host 0.0.0.0 --clear_datastore true .
