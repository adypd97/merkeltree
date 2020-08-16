# merkeltree

- [example1](https://github.com/sangeeths/merkle-tree)
- [example2](https://github.com/JaeDukSeo/Simple-Merkle-Tree-in-Python)

### References
- [merkeltreePDF](http://www.mit.edu/~rio/merkle.pdf)
- [merketreePPT](http://www.cs.tau.ac.il/~msagiv/courses/blockchain/merkel.pdf)
- [merkeltree1](https://brilliant.org/wiki/merkle-tree/)

toy merkel tree with demo, for fun and learning

### DEMO
- There are two files, ```client.py``` and ```server.py```
- Open two terminals and run both of the above mentioned files
  in each one like so.

  ```./client.py <clientfile>``` AND ```./server.py <serverfile>```
- If the two files namely, clientfile.txt and serverfile.txt are exactly 
  the same then the server would reply with a consistent reponse
- If not, then the server would respond with an inconsistent reponse
  and close connection.
- (UNDER CONSTRUCTION) Server sends back the changed chunks only to the 
  client so the client can reconstruct with the ground truth file (ie.
  the serverfile)

### V0
-  Support for individual files only. Checks integrity of file.

-  IMPLEMENTING ONLY A CLIENT SERVER MODEL, LATER P2P.

- HOW IT WORKS?

 STEP 1. Client requests the hash of a file, expecting 
         it to match with the current hash that it has access to
	 of that same file.
 STEP 2. Client checks if the two match, if yes, then we are done
         and know that file hasn't changed on server. else we report error
	 (saying that the file was changed)
 STEP 3: Client doesn't report error right away as in STEP 2. It
         requests further hashes down to the leaf nodes of merkel tree 
         to find out which chunk(s) of data were changed.
 STEP 4: Then it requests for those chunks only. On receiving 
         the server recalculates the root hash.

### SOME NOTES

- The hashes are stored in the Merkle Tree. They are sent to the client
  on request. 

- There are two file, clientfile.txt and serverfile.txt. These represent the 
  the files the client and server has access to respectively. We are trying 
  to simulate client and server on two different computers that are communicating
  for the file serverfile.txt( this is the most up to date file, and all clients
  must have this version to stay up to date).

