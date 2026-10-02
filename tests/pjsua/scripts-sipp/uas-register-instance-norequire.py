#
# As uas-register-outbound-norequire, with --always-instance-id: the refresh
# keeps +sip.instance. SIPp checks the REGISTERs, see the XML scenario.
#
PJSUA = ['--null-audio --always-instance-id']

# Add the account only once SIPp listens: a start-up REGISTER would be
# refused, and an "rr" racing it could be lost to PJSIP_EBUSY.
PJSUA_EXPECTS = [[0, "", "+a sip:pjsua@127.0.0.1 "
                         "sip:127.0.0.1:$SIPP_PORT;transport=tcp * pjsua pjsua"]]

SIPP_TRANSPORT = "t1"
