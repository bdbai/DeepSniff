# DeepSniff

Use artificial neural network to sniff protocols.

## Provisional feature vector

- 8 numbers of entropies of first 8 packets
- 8 numbers of (lengths / MTU) of first 8 packets
- 8 booleans (1 for true, 0 for false) of whether the nth packet contains only ASCII characters
- 1 number of the entropy of lengths of first 8 packets

File an issue if you think more features should be added.

## Provisional output vector

The probabilities that the given feature is that of following protocols:

- Shadowsocks with different ciphers
- Lantern
- ShadowsocksR with different ciphers and protocols and obfss
- V2Ray
- SSH
- Tor
- HTTP
- HTTPS
- Other

The results go through softmax regression.

File an issue if you think more protocols should be added.

## Neural network structure

Undecided yet, might not be too deep.

## Training data needed

If you can provide labeled training data or want to contribute to this project, we welcome you to join the pipesocks team.
