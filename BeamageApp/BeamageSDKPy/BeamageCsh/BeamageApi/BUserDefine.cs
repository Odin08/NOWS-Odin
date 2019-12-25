// Decompiled with JetBrains decompiler
// Type: BeamageApi.BUserDefine
// Assembly: BeamageSDK, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 7DD81749-9415-4B3E-9AD3-5A446061908F
// Assembly location: D:\Laboratory\C#test\Beamage SDK Examples\Beamage SDK C# Simple Viewer Example\Beamage SDK C Sharp Simple Viewer Example\BeamageSDK.dll

namespace BeamageApiCode
{
  internal class BUserDefine
  {
    public const float INITIAL_EXP_TIME_MS = 200f;
    public const float MAX_EXPOSURE_TIME = 5000f;
    public const float MIN_EXPOSURE_TIME = 0.06f;
    public const int TOGGLE_ASK_IMAGE_REGISTER = 128;
    public const float PIXEL_SIZE_GENTEC_CAM = 5.5f;
    public const int NUMBER_OF_VERIFICATION_PACKET = 0;
    public const int CMOS_REG_001_N_LINES_LSB_4M = 0;
    public const int CMOS_REG_001_N_LINES_LSB_2M = 64;
    public const int CMOS_REG_002_N_LINES_MSB_4M = 8;
    public const int CMOS_REG_002_N_LINES_MSB_2M = 4;
    public const int CMOS_REG_035_SUB_S_LSB_NO_SKIP = 0;
    public const int CMOS_REG_035_SUB_S_LSB_SKIP = 1;
    public const int CMOS_REG_037_SUB_A_LSB_NO_SKIP = 0;
    public const int CMOS_REG_037_SUB_A_LSB_SKIP = 1;
    public const int CMOS_REG_039_MONO = 1;
    public const int CMOS_REG_041_EXT_TRIG_OFF_INTE_SYNC = 0;
    public const int CMOS_REG_041_EXT_TRIG_ON_EXP_EXT = 1;
    public const int CMOS_REG_042_EXP_TIME_200_MS = 175;
    public const int CMOS_REG_043_EXP_TIME_200_MS = 75;
    public const int CMOS_REG_044_EXP_TIME_200_MS = 0;
    public const int CMOS_REG_048_EXP_KP1 = 1;
    public const int CMOS_REG_051_EXP_KP2 = 1;
    public const int CMOS_REG_054_NR_SLOPES = 1;
    public const int CMOS_REG_055_EXP_SEQ = 1;
    public const int CMOS_REG_056_EXP_TIME2_200_MS = 175;
    public const int CMOS_REG_057_EXP_TIME2_200_MS = 75;
    public const int CMOS_REG_058_EXP_TIME2_200_MS = 0;
    public const int CMOS_REG_062_DO_NOT_CHANGE = 1;
    public const int CMOS_REG_065_DO_NOT_CHANGE = 1;
    public const int CMOS_REG_068_NR_SLOPES2 = 1;
    public const int CMOS_REG_069_EXP2_SEQ = 1;
    public const int CMOS_REG_070_NUM_FRAMES_LSB = 1;
    public const int CMOS_REG_072_OUTPUT_MODE_12_B = 2;
    public const int CMOS_REG_072_OUTPUT_MODE_10_B = 0;
    public const int CMOS_REG_073_FOT_LENGTH = 10;
    public const int CMOS_REG_074_I_LVDS_REC = 1;
    public const int CMOS_REG_075_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_076_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_078_TRAINING_PARTTERN_LSB = 85;
    public const int CMOS_REG_080_CHANNEL_EN_12_B = 34;
    public const int CMOS_REG_080_CHANNEL_EN_10_B = 255;
    public const int CMOS_REG_081_CHANNEL_EN_12_B = 34;
    public const int CMOS_REG_081_CHANNEL_EN_10_B = 255;
    public const int CMOS_REG_082_CLKCHAN_CTRLCHAN_LVDSCLK = 7;
    public const int CMOS_REG_083_I_LVDS = 8;
    public const int CMOS_REG_084_L_COL = 4;
    public const int CMOS_REG_085_L_COL_PERCH = 1;
    public const int CMOS_REG_086_I_ADC_CMV2000 = 8;
    public const int CMOS_REG_086_I_ADC_CMV4000 = 14;
    public const int CMOS_REG_087_L_AMP = 12;
    public const int CMOS_REG_088_VTF_L1 = 64;
    public const int CMOS_REG_089_VLOW2 = 96;
    public const int CMOS_REG_090_VLOW3 = 96;
    public const int CMOS_REG_091_VRES_LOW = 64;
    public const int CMOS_REG_092_DO_NOT_CHANGE = 96;
    public const int CMOS_REG_093_DO_NOT_CHANGE = 96;
    public const int CMOS_REG_094_V_PRECH = 101;
    public const int CMOS_REG_095_V_REF = 106;
    public const int CMOS_REG_096_DO_NOT_CHANGE = 96;
    public const int CMOS_REG_097_DO_NOT_CHANGE = 96;
    public const int CMOS_REG_098_CAL_DEF12_VRAMP1 = 109;
    public const int CMOS_REG_099_CAL_DEF12_VRAMP2 = 109;
    public const int CMOS_REG_100_CAL_DEF12_OFFSET_LSB = 134;
    public const int CMOS_REG_101_CAL_DEF12_OFFSET_MSB = 62;
    public const int CMOS_REG_102_CAL_DEF12_PGA_GAIN = 1;
    public const int CMOS_REG_103_CAL_DEF12_ADC_GAIN = 57;
    public const int CMOS_REG_121_CAL_DEF12_PGA_GAIN = 0;
    public const int CMOS_REG_098_CAL_DEF10_VRAMP1 = 108;
    public const int CMOS_REG_099_CAL_DEF10_VRAMP2 = 108;
    public const int CMOS_REG_100_CAL_DEF10_OFFSET_LSB = 139;
    public const int CMOS_REG_101_CAL_DEF10_OFFSET_MSB = 63;
    public const int CMOS_REG_102_CAL_DEF10_PGA_GAIN = 1;
    public const int CMOS_REG_103_CAL_DEF10_ADC_GAIN = 57;
    public const int CMOS_REG_121_CAL_DEF10_PGA_GAIN = 0;
    public const int CALIBRATION_NUMBER_OF_REGISTERS = 7;
    public const int CMOS_REG_098_CAL_DEF_VRAMP1_MIN = 102;
    public const int CMOS_REG_098_CAL_DEF_VRAMP1_MAX = 115;
    public const int CMOS_REG_099_CAL_DEF_VRAMP2_MIN = 102;
    public const int CMOS_REG_099_CAL_DEF_VRAMP2_MAX = 115;
    public const int CMOS_REG_100_CAL_DEF_OFFSET_LSB_MIN = 0;
    public const int CMOS_REG_100_CAL_DEF_OFFSET_LSB_MAX = 255;
    public const int CMOS_REG_101_CAL_DEF_OFFSET_MSB_MIN = 59;
    public const int CMOS_REG_101_CAL_DEF_OFFSET_MSB_MAX = 64;
    public const int CMOS_REG_102_CAL_DEF_PGA_GAIN_MIN = 0;
    public const int CMOS_REG_102_CAL_DEF_PGA_GAIN_MAX = 3;
    public const int CMOS_REG_103_CAL_DEF_ADC_GAIN_MIN = 54;
    public const int CMOS_REG_103_CAL_DEF_ADC_GAIN_MAX = 61;
    public const int CMOS_REG_121_CAL_DEF_PGA_GAIN_MIN = 0;
    public const int CMOS_REG_121_CAL_DEF_PGA_GAIN_MAX = 1;
    public const int CALIBRATION_IMBRICATION = 64;
    public const int CMOS_REG_104_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_105_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_106_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_107_DO_NOT_CHANGE = 8;
    public const int CMOS_REG_108_T_DIG1 = 2;
    public const int CMOS_REG_109_T_DIG2 = 4;
    public const int CMOS_REG_111_BIT_MODE_12_B = 0;
    public const int CMOS_REG_111_BIT_MODE_10_B = 1;
    public const int CMOS_REG_112_ADC_RES_12_B = 2;
    public const int CMOS_REG_112_ADC_RES_10_B = 0;
    public const int CMOS_REG_113_PLL_EN_ON = 1;
    public const int CMOS_REG_113_PLL_EN_OFF = 0;
    public const int CMOS_REG_114_PLL_IN_FRE_10_15_MHZ = 1;
    public const int CMOS_REG_115_PLL_BYPASS_ON = 1;
    public const int CMOS_REG_115_PLL_BYPASS_OFF = 0;
    public const int CMOS_REG_116_PLL_R_F_D_10_15_MHZ_12_B = 43;
    public const int CMOS_REG_116_PLL_R_F_D_10_15_MHZ_10_B = 41;
    public const int CMOS_REG_117_PLL_LOAD_12_B = 4;
    public const int CMOS_REG_117_PLL_LOAD_10_B = 8;
    public const int CMOS_REG_118_DUMMY_DEFAULT = 0;
    public const int CMOS_REG_123_V_BLACKSUN_DEFAULT = 98;
    public const int FPGA_REG_128_RESET_STATE = 128;
    public const int FPGA_REG_128_CLEAR_REG = 0;
    public const int FPGA_REG_128_CMOS_READ = 2;
    public const int FPGA_REG_128_SET_GRAB_FRAME = 1;
    public const int FPGA_REG_128_MASK_RESET = 127;
    public const int FGPA_REG_129_12_B = 0;
    public const int FGPA_REG_129_10_B = 8;
    public const int FGPA_REG_129_MASK_EEPROM_READ_CLEAR = 254;
    public const int FGPA_REG_129_MASK_EEPROM_READ = 1;
    public const int FGPA_REG_129_MASK_EEPROM_WRITE_CLEAR = 253;
    public const int FGPA_REG_129_SET_EEPROM_WRITE = 2;
    public const int FGPA_REG_129_SET_EEPROM_ERASE = 4;
    public const int FGPA_REG_129_MASK_EEPROM_ERASE_CLEAR = 251;
    public const int FPGA_REG_129_MASK_USE_EXT_TRIG = 64;
    public const int FPGA_REG_129_MASK_NOT_USE_EXT_TRIG = 191;
    public const int FGPA_REG_134_GREEN_LED_ON = 1;
    public const int FGPA_REG_134_MASK_AVG_OFF = 127;
    public const int FGPA_REG_134_MASK_AVG_ON = 128;
    public const int FGPA_REG_134_SET_TRIG_ON = 32;
    public const int FGPA_REG_134_MASK_TRIG_OFF = 223;
    public const int FGPA_REG_140_PIX_OUT_OF_NONE = 1;
    public const int FGPA_REG_140_PIX_OUT_OF_DECIMATE = 2;
    public const int ADC_BIT_NUMBER_GENTEC = 12;
    public const int MAX_IMAGE_WIDTH_SIZE = 2048;
    public const float CMOSIS_CLK_IN_FREQ = 1.5E+08f;
    public const int CMOSIS_REG73 = 10;

    public enum PixelAdressing
    {
      NONE,
      AVERAGE,
      DECIMATE,
      BINNING,
    }

    public enum AdressingValue
    {
      NONE = 1,
      ACTIVE = 2,
    }
  }
}
