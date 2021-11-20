
static const CPU_INT08U CPU_CntLeadZerosTbl[256] = {
    /* Data vals :                      */
    /*   0    1    2    3    4    5    6    7    8    9    A    B    C    D    E    F   */
    8u, 7u, 6u, 6u, 5u, 5u, 5u, 5u, 4u, 4u, 4u, 4u, 4u, 4u, 4u, 4u, /*   0x00 to 0x0F   */
    3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, 3u, /*   0x10 to 0x1F   */
    2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, /*   0x20 to 0x2F   */
    2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, 2u, /*   0x30 to 0x3F   */
    1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, /*   0x40 to 0x4F   */
    1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, /*   0x50 to 0x5F   */
    1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, /*   0x60 to 0x6F   */
    1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, 1u, /*   0x70 to 0x7F   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0x80 to 0x8F   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0x90 to 0x9F   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0xA0 to 0xAF   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0xB0 to 0xBF   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0xC0 to 0xCF   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0xD0 to 0xDF   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, /*   0xE0 to 0xEF   */
    0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u, 0u  /*   0xF0 to 0xFF   */
};

/*8bit类型数据计算前导零*/
CPU_DATA CPU_CntLeadZeros08(CPU_INT08U val)
{
    CPU_DATA ix;
    CPU_DATA nbr_lead_zeros;
    /* ----------- C-OPTIMIZED ------------ */
    /* Chk bits [07:00] :                   */
    /* .. Nbr lead zeros =               .. */
    /* .. lookup tbl ix  = 'val' >>  0 bits */
    ix = (CPU_DATA)(val >> 0u); 
    /* .. plus nbr msb lead zeros =  0 bits.*/                               
    nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 0u); 

    return (nbr_lead_zeros);
}

/*16bit类型数据计算前导零*/
CPU_DATA CPU_CntLeadZeros16(CPU_INT16U val)
{
    CPU_DATA ix;
    CPU_DATA nbr_lead_zeros;
    if (val > 0x00FFu)
    {   /* Chk bits [15:08] :                   */
        /* .. Nbr lead zeros =               .. */
        /* .. lookup tbl ix  = 'val' >>  8 bits */
        ix = (CPU_DATA)(val >> 8u);  
        /* .. plus nbr msb lead zeros =  0 bits.*/                              
        nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 0u); 
    }
    else
    {   /* Chk bits [07:00] :                   */
        /* .. Nbr lead zeros =               .. */
        /* .. lookup tbl ix  = 'val' >>  0 bits */
        ix = (CPU_DATA)(val >> 0u);
        /* .. plus nbr msb lead zeros =  8 bits.*/                                
        nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 8u); 
    }
    return (nbr_lead_zeros);
}

/*32bit类型数据计算前导零*/
CPU_DATA CPU_CntLeadZeros32(CPU_INT32U val)
{

    CPU_DATA ix;
    CPU_DATA nbr_lead_zeros;
    /* ---------- ASM-OPTIMIZED ----------- */
    if (val > 0x0000FFFFu)
    {
        if (val > 0x00FFFFFFu)
        {   /* Chk bits [31:24] :                   */
            /* .. Nbr lead zeros =               .. */
            /* .. lookup tbl ix  = 'val' >> 24 bits */
            ix = (CPU_DATA)(val >> 24u);
            /* .. plus nbr msb lead zeros =  0 bits.*/                               
            nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 0u); 
        }
        else
        {   /* Chk bits [23:16] :                   */
            /* .. Nbr lead zeros =               .. */
            /* .. lookup tbl ix  = 'val' >> 16 bits */
            ix = (CPU_DATA)(val >> 16u); 
            /* .. plus nbr msb lead zeros =  8 bits.*/                              
            nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 8u); 
        }
    }
    else
    {
        if (val > 0x000000FFu)
        {   /* Chk bits [15:08] :                   */
            /* .. Nbr lead zeros =               .. */
            /* .. lookup tbl ix  = 'val' >>  8 bits */
            ix = (CPU_DATA)(val >> 8u);
            /* .. plus nbr msb lead zeros = 16 bits.*/                                 
            nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 16u); 
        }
        else
        {   /* Chk bits [07:00] :                   */
            /* .. Nbr lead zeros =               .. */
            /* .. lookup tbl ix  = 'val' >>  0 bits */
            ix = (CPU_DATA)(val >> 0u);
            /* .. plus nbr msb lead zeros = 24 bits.*/                                 
            nbr_lead_zeros = (CPU_DATA)(CPU_CntLeadZerosTbl[ix] + 24u); 
        }
    }

    return (nbr_lead_zeros);
}