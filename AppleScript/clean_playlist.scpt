tell application "Music"
  -- Get all tracks in specified playlist
  set dialog_output to display dialog "Playlist to clean" default answer "" with icon note buttons {"Cancel", "Continue"} default button "Continue"
  set playlist_name to text returned of dialog_output
  set tr to tracks of playlist playlist_name
  set names_of_doomed to {}
  set doomed to {}
  
  -- For each track in the playlist get the last skipped date, last played date, and if it's disliked
  repeat with t in tr
    set last_played_date to get played date of t
    set last_skipped_date to get skipped date of t
    set is_disliked to get disliked of t
    set played_count to get played count of t

    if last_played_date is equal to last_skipped_date and played_count is greater than 1 then
      set name_of_doomed to get name of t
      copy name_of_doomed to end of names_of_doomed
      copy t to end of doomed
    end if
  end repeat
    
    -- If the track was skipped last time it was played or it is disliked then remove it from the playlist
  display dialog "Going to delete " & names_of_doomed buttons {"Don't do it", "Continue"} default button "Continue" cancel button "Don't do it"
  if button returned of result = "Continue" then
    repeat with t in doomed
      tell playlist "Jonathan" to delete t
    end repeat
  end if
end tell
