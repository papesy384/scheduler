#!/bin/bash

# Auto-refresh browser script for scheduler
echo "🔄 Refreshing browser..."

# Try to refresh different browsers
osascript -e 'tell application "Google Chrome" to reload active tab of front window' 2>/dev/null || \
osascript -e 'tell application "Safari" to do JavaScript "location.reload()" in document 1' 2>/dev/null || \
echo "⚠️ Could not refresh browser automatically"

echo "✅ Browser refresh attempted"
