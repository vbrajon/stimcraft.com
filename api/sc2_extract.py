import os
import sys
from importlib import import_module
import mpyq
import s2protocol

# s2protocol.versions/__init__.py imports `imp`, removed in Python 3.12 (Blizzard/s2protocol#130).
# Protocol files only depend on s2protocol.decoders, so import them as top-level modules.
sys.path.append(os.path.join(os.path.dirname(s2protocol.__file__), 'versions'))
protocol15405 = import_module('protocol15405')


# Game events (raw player inputs) are skipped: they are most of the decoding time and of the payload.
def sc2_extract(replay_file):
    archive = mpyq.MPQArchive(replay_file)
    # The header reads with any protocol; its base build selects the protocol of the rest
    header = protocol15405.decode_replay_header(archive.header['user_data_header']['content'])
    protocol = import_module('protocol%s' % header['m_version']['m_baseBuild'])
    details = protocol.decode_replay_details(archive.read_file('replay.details'))
    del details['m_cacheHandles']
    initdata = protocol.decode_replay_initdata(archive.read_file('replay.initData'))
    del initdata['m_syncLobbyState']['m_gameDescription']['m_cacheHandles']
    return {
        'header': header,
        'details': details,
        'initdata': initdata,
        'messageevents': list(protocol.decode_replay_message_events(archive.read_file('replay.message.events'))),
        'trackerevents': list(protocol.decode_replay_tracker_events(archive.read_file('replay.tracker.events'))),
        'attributeevents': protocol.decode_replay_attributes_events(archive.read_file('replay.attributes.events')),
    }
