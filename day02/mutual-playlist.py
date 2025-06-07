my_playlist = {
    "All I Want for Christmas Is You",
    "Silent Night, Holy Night",
    "Star Ng Pasko",
    "Pasko Na Sinta Ko"
}
friend_playlist = {
    "Baby, It's Cold Outside",
    "All I Want for Christmas Is You",
    "Kampana ng Simbahan",
    "Christmas Bonus"
}
combined_playlist = my_playlist & friend_playlist

print(*combined_playlist, sep="\n")