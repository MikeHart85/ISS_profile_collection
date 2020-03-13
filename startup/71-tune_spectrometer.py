


tune_pcl =  [{'motor': six_axes_stage.yaw.name,
                   'detector': bpm_fm.name,
                   'range': 0.1,
                   'step': 0.001,
                   'retries': 3,
                   'comment': 'Yaw tune'},
                  {'motor': six_axes_stage.pitch.name,
                   'detector': bpm_fm.name,
                   'range': 1,
                   'step': 0.01,
                   'retries': 3,
                   'comment': 'Pitch tune'},
                  {'motor': six_axes_stage.x.name,
                   'detector': bpm_fm.name,
                   'range': 1,
                   'step': 0.01,
                   'retries': 3,
                   'comment': 'X tune'},
                  {'motor': six_axes_stage.y.name,
                   'detector': bpm_fm.name,
                   'range': 1,
                   'step': 0.01,
                   'retries': 3,
                   'comment': 'Y tune'},
                ]

# def tune_beamline_plan(stdout=sys.stdout):
#
#     print_to_gui(f'[Beamline tuning] Starting...',stdout=stdout)
#     yield from bps.mv(hhm.fb_status,0)
#
#
#     yield from bps.mv(bpm_fm,'insert')
#
#
#
#     for element in tune_elements:
#         detector = detector_dictionary[element['detector']]['obj']
#         motor = motor_dictionary[element['motor']]['object']
#         yield from tuning_scan(motor, detector,
#                               element['range'],
#                               element['step'],
#                               retries=element['retries'],
#                               stdout=stdout
#                               )
#         # turn camera into continuous mode
#         if hasattr(detector, 'image_mode'):
#             yield from bps.mv(getattr(detector, 'image_mode'), 2)
#             yield from bps.mv(getattr(detector, 'acquire'), 1)
#
#     yield from bps.mv(bpm_fm, 'retract')
#     print('[Beamline tuning] Beamline tuning complete')