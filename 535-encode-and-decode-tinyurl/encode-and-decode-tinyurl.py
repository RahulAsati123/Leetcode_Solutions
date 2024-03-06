class Codec:

    def encode(self, longUrl: str) -> str:
        m = {}
        for i in longUrl:
            m[i] = chr(ord(i)+1)
        en_string = ""
        for i in longUrl:
            en_string += m[i]
        return en_string
        
        
        """Encodes a URL to a shortened URL.
        """
        

    def decode(self, shortUrl: str) -> str:
        de_string = ""
        for i in shortUrl:
            de_string += chr(ord(i)-1)
        return de_string
       
    
        """Decodes a shortened URL to its original URL.
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))