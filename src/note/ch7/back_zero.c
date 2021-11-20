#define NVM_CRC_QUEUE_ENTRY_BITS (32u)

uint8 NvM_CrcQueueCountTrailingZeros(uint32 Word)
{
    uint8 trailingZeroes = 0u;

    if(Word == 0u)
    {   /* special condition -> avoid going through the divide and conquer algorithm below.  *
         * => it would require additional handling at the remaining two bits.               */
        trailingZeroes = NVM_CRC_QUEUE_ENTRY_BITS;
    }
    else
    {
        uint32 currWord = Word;
        /* is none of the lower 16 bits set? */
        if((currWord & 0xFFFFu) == 0u)
        {
            trailingZeroes |= 0x10u;
            currWord >>= 16u;
        }

        /* is none of the lower 8bits set? */
        if((currWord & 0xFFu) == 0u)
        {
            trailingZeroes |= 0x08u;
            currWord >>= 8u;
        }

        /* is none of the lower 4 bits set?*/
        if((currWord & 0x0Fu) == 0u)
        {
            trailingZeroes |= 0x04u;
            currWord >>= 4u;
        }

        /* is none of the lower 2 bits set? */
        if((currWord & 0x03u) == 0u)
        {
            trailingZeroes |= 2u;
            currWord >>= 2u;
        }

        /* Process least significant bit.
        * If the least significant bit is zero, add 1, because the second one cannot be cleared
        * Initially, we checked for word == 0, therefore one of both bits must be set here
        * If LSB is set, add nothing.
        * The cast appears to be unnecessary. However, some Compilers might issue a warning,
        * if uint16_least is 16bit, while QueueBitMask is 32bit width */
        trailingZeroes |= (uint8)((currWord & 1u) ^ 1u);
    }

    return trailingZeroes;
}