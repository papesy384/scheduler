#!/usr/bin/env python3
"""
Auto-refresh script for the scheduler
This script monitors file changes and automatically refreshes the browser
"""

import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SchedulerRefreshHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_refresh = 0
        self.refresh_cooldown = 2  # Minimum seconds between refreshes
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Only watch HTML files
        if event.src_path.endswith('.html'):
            current_time = time.time()
            if current_time - self.last_refresh > self.refresh_cooldown:
                print(f"🔄 File changed: {os.path.basename(event.src_path)}")
                print("🌐 Refreshing browser...")
                
                # Refresh browser (works on macOS)
                subprocess.run(['osascript', '-e', 'tell application "Safari" to do JavaScript "location.reload()" in document 1'], 
                             capture_output=True)
                
                # Also try Chrome if Safari doesn't work
                subprocess.run(['osascript', '-e', 'tell application "Google Chrome" to reload active tab of front window'], 
                             capture_output=True)
                
                self.last_refresh = current_time
                print("✅ Browser refreshed!")

def main():
    print("🚀 Starting auto-refresh monitor for scheduler...")
    print("📁 Watching: /Users/macbook/Desktop/scheduler/")
    print("🌐 Browser will auto-refresh when files change")
    print("⏹️  Press Ctrl+C to stop")
    
    event_handler = SchedulerRefreshHandler()
    observer = Observer()
    observer.schedule(event_handler, '/Users/macbook/Desktop/scheduler/', recursive=False)
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Auto-refresh stopped")
    
    observer.join()

if __name__ == "__main__":
    main()
