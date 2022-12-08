# apple script to watch for three finger swipe down and then print a dialog box saying
# "three finger swipe down"
tell application "System Events"
    tell process "Dock"
        repeat
            set threeFingerSwipeDown to (event type of next event) is equal to "threeFingerSwipeDown"
            if threeFingerSwipeDown then
                display dialog "three finger swipe down"
            end if
        end repeat
    end tell
end tell