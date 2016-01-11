class Song:

    def __init__(self,title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def length(self, seconds=False, minutes = False, hours = False):
        len_sec = 0
        len_min = 0
        len_hr = 0
        length_str = self.length.split(':')
        if seconds:
            if len(length_str) == 3:
                len_sec+= 3600*length_str[0]+60*length_str[1]+length_str[2]
            elif len(length_str) == 2:
                len_sec+=60*length_str[0]+length_str[1]
            return len_sec

        if minutes:
            if len(length_str) == 3:
                len_min+=60*length_str[0]+length_str[1]
            elif len(length_str) == 2:
                len_min+=length_str[0]
            return len_min

        if hours:
            if len(length_str) == 3:
                len_hr+=length_str[0]
            return len_hr

        return self.length
