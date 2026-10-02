#
# pjsua never offers SIP outbound over UDP, so --always-instance-id is the
# only source of +sip.instance here. SIPp checks the REGISTER, see the XML
# scenario.
#
PJSUA = ['--null-audio --id=sip:pjsua@127.0.0.1 --registrar=$SIPP_URI '
         '--realm=* --username=pjsua --password=pjsua --always-instance-id']

PJSUA_EXPECTS = []
