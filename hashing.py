from Crypto.Hash import SHA256
def read_chunks(file_obj):
	size_of_chunk = 1024
	while True:
		data = file_obj.read(size_of_chunk)
		if not data:
			break
		yield data
def computeHash(fname):

	fh = open(fname,'rb')
	chunks = list()
	for chunk in read_chunks(fh):
		chunks.append(chunk)
		#print(len(chunk))
	i=len(chunks)-1

	hash_t  = bytearray(SHA256.new(chunks[i]).digest())
	print(hash_t)
	print(len(hash_t))
	while i>=1:
	 	data = chunks[i]
	 	hash1 = bytearray(SHA256.new(data).digest())
	 	chunks[i-1] = chunks[i-1]+hash1
	 	# temp1 = list()
	 	# temp1.append(chunks[i-1])
	 	# temp1.append(has)
	 	i-=1
	hash_f = SHA256.new(chunks[i]).hexdigest()
	return hash_f
	

fname = 'final.mp4_download'
final_h = computeHash(fname)
print(final_h)