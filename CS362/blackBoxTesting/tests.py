# Jhonatan Becerra
# Black box testing
# Test generation methodology:
# I thought about the input and how it related to each-other.
# With this in mind, I created a table with the different input, and
# assigned them different states which could be defined as
# correct and incorrect. Then, I simply tested edge values.

import unittest
from credit_card_validator import credit_card_validator


class CardNumber(unittest.TestCase):
    # incorrect input type#######################
    # these inputs were picked outside of the table I created.

    # non string
    def test_incorrect_type(self):
        self.assertFalse(credit_card_validator(4485816481367600))

    # empty string
    def test_empty_string(self):
        self.assertFalse(credit_card_validator(""))

    # non-number string
    def test_non_number(self):
        self.assertFalse(credit_card_validator("abcdefghijklmnop"))

    # zeroes
    def test_zero(self):
        self.assertFalse(credit_card_validator("0000000000000000"))

    # max value
    def test_max_value(self):
        self.assertFalse(credit_card_validator("9999999999999999"))

    # Visa ##################################
    # these values were generated using a table.
    # the change in states can be observed by reading the comments

    # correct prefix, correct length, correct checksum
    # random value known to be valid
    def test_visa_cp_cl_cs(self):
        self.assertTrue(credit_card_validator("4485816481367600"))

    # incorrect size, match with size of amex
    # this value was chosen because it is the same size as
    # the input for amex
    def test_visa_cls(self):
        self.assertFalse(credit_card_validator("411111111111116"))

    # edge low
    # test low edge of visa prefix
    def test_visa_edge_low(self):
        self.assertTrue(credit_card_validator("4111111111111111"))

    # edge high
    # test high edge of visa prefix
    def test_visa_edge_high(self):
        self.assertTrue(credit_card_validator("4999999999999996"))

    # for these values generated from a table, I established a
    # naming convention.
    # c = correct, i = incorrect, p = prefix, l= length, s = checksum

    # from table
    # incorrect prefix, correct length, correct checksum
    def test_visa_ip_cl_cs(self):
        self.assertFalse(credit_card_validator("0485816481367608"))

    # ilof = incorrect length overflow. This means the number length
    # was larger than expected.
    # correct prefix, incorrect length (overflow), correct checksum
    def test_visa_cp_ilof_cs(self):
        self.assertFalse(credit_card_validator("448581648136760000"))

    # iluf = incorrect length underflow. This means the number length
    # was shorter than expected
    # correct prefix, incorrect length (underflow), correct checksum
    def test_visa_cp_iluf_cs(self):
        self.assertFalse(credit_card_validator("44858164813676"))

    # correct prefix, correct length, incorrect checksum
    def test_visa_cp_cl_is(self):
        self.assertFalse(credit_card_validator("4485816481367609"))

    # incorrect prefix, incorrect length (overflow), correct checksum
    def test_visa_ip_ilof_cs(self):
        self.assertFalse(credit_card_validator("048581648136760008"))

    # incorrect prefix, incorrect length (underflow), correct checksum
    def test_visa_ip_iluf_cs(self):
        self.assertFalse(credit_card_validator("04858164813674"))

    # incorrect prefix, correct length, incorrect checksum
    def test_visa_ip_cl_is(self):
        self.assertFalse(credit_card_validator("0485816481367600"))

    # correct prefix, incorrect length (overflow), incorrect checksum
    def test_visa_cp_ilof_is(self):
        self.assertFalse(credit_card_validator("448581648136760001"))

    # correct prefix, incorrect length (underflow), incorrect checksum
    def test_visa_cp_iluf_is(self):
        self.assertFalse(credit_card_validator("44858164813671"))

    # incorrect prefix, incorrect length, incorrect checksum
    def test_visa_ip_il_is(self):
        self.assertFalse(credit_card_validator("0485816413671"))

    # Mastercard #############################################################3
    # correct prefix, correct length, correct checksum
    def test_master_cp_cl_cs(self):
        self.assertTrue(credit_card_validator("2221002185316010"))

    # edge low, low prefix
    def test_master_edge_low_lp(self):
        self.assertTrue(credit_card_validator("5111111111111118"))

    # edge low, high prefix
    def test_master_edge_low_hp(self):
        self.assertTrue(credit_card_validator("5199999999999991"))

    # edge high, low prefix
    def test_master_edge_high_lp(self):
        self.assertTrue(credit_card_validator("2720111111111118"))

    # edge high, high prefix
    def test_master_edge_high_hp(self):
        self.assertTrue(credit_card_validator("2720999999999996"))

    # incorrect prefix, correct length, correct checksum
    def test_master_ip_cl_cs(self):
        self.assertFalse(credit_card_validator("9221002185316015"))

    # correct prefix, incorrect length (overflow), correct checksum
    def test_master_cp_ilof_cs(self):
        self.assertFalse(credit_card_validator("222100218531601018"))

    # correct prefix, incorrect length (underflow), correct checksum
    def test_master_cp_iluf_cs(self):
        self.assertFalse(credit_card_validator("22210021853162"))

    # correct prefix, correct length, incorrect checksum
    def test_master_cp_cl_is(self):
        self.assertFalse(credit_card_validator("2221002185316019"))

    # incorrect prefix, incorrect length (overflow), correct checksum
    def test_master_ip_ilof_cs(self):
        self.assertFalse(credit_card_validator("922100218531601013"))

    # incorrect prefix, incorrect length (underflow), correct checksum
    def test_master_ip_iluf_cs(self):
        self.assertFalse(credit_card_validator("9221002185316015"))

    # incorrect prefix, correct length, incorrect checksum
    def test_master_ip_cl_is(self):
        self.assertFalse(credit_card_validator("9221002185316016"))

    # correct prefix, incorrect length (overflow), incorrect checksum
    def test_master_cp_ilof_is(self):
        self.assertFalse(credit_card_validator("222100218531601011"))

    # correct prefix, incorrect length (underflow), incorrect checksum
    def test_master_cp_iluf_is(self):
        self.assertFalse(credit_card_validator("22210021853160"))

    # incorrect prefix, incorrect length, incorrect checksum
    def test_master_ip_il_is(self):
        self.assertFalse(credit_card_validator("922100218531601"))

    # AMEX ############################################################
    # correct prefix, correct length, correct checksum
    def test_amex_cp_cl_cs(self):
        self.assertTrue(credit_card_validator("349481180538680"))

    # incorrect prefix, correct length, correct checksum
    def test_amex_ip_cl_cs(self):
        self.assertFalse(credit_card_validator("357118047583405"))

    # correct prefix, incorrect length (overflow), correct checksum
    def test_amex_cp_ilof_cs(self):
        self.assertFalse(credit_card_validator("3494811805386809"))

    # correct prefix, incorrect length (underflow), correct checksum
    def test_amex_cp_iluf_cs(self):
        self.assertFalse(credit_card_validator("34948118053867"))

    # correct prefix, correct length, incorrect checksum
    def test_amex_cp_cl_is(self):
        self.assertFalse(credit_card_validator("349481180538681"))

    # incorrect prefix, incorrect length (overflow), correct checksum
    def test_amex_ip_ilof_cs(self):
        self.assertFalse(credit_card_validator("3594811805386808"))

    # incorrect prefix, incorrect length (underflow), correct checksum
    def test_amex_ip_iluf_cs(self):
        self.assertFalse(credit_card_validator("35948118053866"))

    # incorrect prefix, correct length, incorrect checksum
    def test_amex_ip_cl_is(self):
        self.assertFalse(credit_card_validator("359481180538688"))

    # correct prefix, incorrect length (overflow), incorrect checksum
    def test_amex_cp_ilof_is(self):
        self.assertFalse(credit_card_validator("3494811805386801"))

    # correct prefix, incorrect length (underflow), incorrect checksum
    def test_amex_cp_iluf_is(self):
        self.assertFalse(credit_card_validator("34948118053868"))

    # incorrect prefix, incorrect length, incorrect checksum
    def test_amex_ip_il_is(self):
        self.assertFalse(credit_card_validator("35948118053868"))


if __name__ == '__main__':
    unittest.main()
