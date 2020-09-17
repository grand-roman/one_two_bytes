# one_two_bytes

// Input: we have an array of bytes that encode some text symbols/chars
// Each symbol can be encoded with 1 or 2 bytes
// If symbol is encoded with 1 byte then it's high bit equals to 1
// If symbol is encoded with 2 bytes then first byte has high bit equal to 0 while second byte can have any value for the high bit (0 or 1) because we know that there is no 3,4,5... bytes symbols
// Challenge: Create a function that has as input specified array and it's length and finds out whether last symbol in this array is 1 or 2-bytes long
