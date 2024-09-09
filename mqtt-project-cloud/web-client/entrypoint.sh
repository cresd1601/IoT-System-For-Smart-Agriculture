#!/bin/sh

echo "Check that we have NEXT_PUBLIC_CLOUD_SERVICE_IP vars"
test -n "$NEXT_PUBLIC_CLOUD_SERVICE_IP"

find /app/.next \( -type d -name .git -prune \) -o -type f -print0 | xargs -0 sed -i "s#APP_NEXT_PUBLIC_CLOUD_SERVICE_IP#$NEXT_PUBLIC_CLOUD_SERVICE_IP#g"

echo "Starting Nextjs"
exec "$@"