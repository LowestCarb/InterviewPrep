Image Cache
Overview
You are to build a simple image cache for holding images in memory. This cache should have a maximum size in bytes. Since the cache has a limited byte size, we will use an LRU algorithm to evict based on which URLs were least recently seen.

The format of the input file will be as follows:

1.	The first line of the input will be an integer indicating the maximum size of the cache in bytes.
2.	The second line will be an integer that indicates the number of URLs (N) that will appear subsequently in the input.
3.	The remaining N lines of the input are URLs representing requests that will be made to the cache.

cache_size_in_bytes
number_of_urls
url_1
url_2
...
url_n


For each URL, your program should attempt to fetch it from the cache, and if it isn't present, download it from the internet and place it in the cache. You should save the entire image in the cache, even though you can achieve the desired output without doing so.

Your output should contain N lines, in the same order as the input. Each line will be formatted as
 <url requested> <IN_CACHE|DOWNLOADED> <size of image in bytes>
 

If you need more images to experiment with, you can use a site like https://placeholdit.imgix.net. For example:
https://placeholdit.imgix.net/~text?txt=image1
https://placeholdit.imgix.net/~text?txt=image2

If you are using a language where making web requests is cumbersome, in order to save time,
you can stub out downloading images with a static	map.

Sample Input
524288
3
http://i.imgur.com/xGmX4h3.jpg
http://i.imgur.com/IUfsijF.jpg
http://i.imgur.com/xGmX4h3.jpg


Sample Output
http://i.imgur.com/xGmX4h3.jpg DOWNLOADED 93606
http://i.imgur.com/IUfsijF.jpg DOWNLOADED 317908
http://i.imgur.com/xGmX4h3.jpg IN_CACHE 93606

