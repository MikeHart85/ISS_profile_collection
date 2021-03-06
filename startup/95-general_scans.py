def constant_energy(name: str, comment: str, n_cycles: int = 1, duration: float = 0, reference = True, **kwargs):

    sys.stdout = kwargs.pop('stdout', sys.stdout)
    uids = []

    for indx in range(int(n_cycles)):
        name_n = '{} {:04d}'.format(name, indx + 1)

        uid = (yield from execute_constant_energy(name_n, duration, comment=comment))
        uids.append(uid)


        yield from bps.sleep(float(delay))
    return uids




def sleep(delay:int=1, **kwargs):
    sys.stdout = kwargs.pop('stdout', sys.stdout)
    print_to_gui(f'Pausing for {delay} seconds....',sys.stdout)
    yield from (bps.sleep(int(delay)))
    print_to_gui(f'Resuming', sys.stdout)



def set_gains_and_offsets(i0_gain:int=5, it_gain:int=5, iff_gain:int=6,
                          ir_gain:int=5, hs:bool=False):
    sys.stdout = kwargs.pop('stdout', sys.stdout)
    i0_gain = int(i0_gain)
    it_gain = int(it_gain)
    iff_gain = int(iff_gain)
    ir_gain = int(ir_gain)
    if type(hs) == str:
        hs = hs == 'True'

    RE(set_gains_and_offsets_plan(i0_amp, i0_gain, hs, it_amp, it_gain, hs, iff_amp, iff_gain, hs, ir_amp, ir_gain, hs))




def set_gains(i0_gain:int=5, it_gain:int=5, iff_gain:int=5,
                          ir_gain:int=5, hs:bool=False, **kwargs):
    sys.stdout = kwargs.pop('stdout', sys.stdout)
    i0_gain = int(i0_gain)
    it_gain = int(it_gain)
    iff_gain = int(iff_gain)
    ir_gain = int(ir_gain)
    if type(hs) == str:
        hs = hs == 'True'

    yield from set_gains_plan(i0_amp, i0_gain, hs, it_amp, it_gain, hs, iff_amp, iff_gain, hs, ir_amp, ir_gain, hs)


def general_scan(detectors, num_name, den_name, result_name, motor, rel_start, rel_stop, num, find_min_max, retries,
                 **kwargs):
    sys.stdout = kwargs.pop('stdout', sys.stdout)
    for index, detector in enumerate(detectors):
        if type(detector) == str:
            detectors[index] = eval(detector)

    if type(motor) == str:
        motor = eval(motor)

    print('[General Scan] Starting scan...')
    ax = kwargs.get('ax')

    if find_min_max:
        over = False
        while (not over):
            uid = RE(general_scan_plan(detectors, motor, rel_start, rel_stop, int(num)),
                     NormPlot(num_name, den_name, result_name, result_name, motor.name, ax=ax))
            yield uid
            last_table = db.get_table(db[-1])
            if detectors[0].polarity == 'pos':
                index = np.argmax(last_table[num_name])
            else:
                index = np.argmin(last_table[num_name])
            motor.move(last_table[motor.name][index])
            print('[General Scan] New {} position: {}'.format(motor.name, motor.position))
            if (num >= 10):
                if (((index > 0.2 * num) and (index < 0.8 * num)) or retries == 1):
                    over = True
                if retries > 1:
                    retries -= 1
            else:
                over = True
        print('[General Scan] {} tuning complete!'.format(motor.name))
    else:
        uid, = RE(general_scan_plan(detectors, motor, rel_start, rel_stop, int(num)),
                  NormPlot(num_name, den_name, result_name, result_name, motor.name, ax=ax))
        yield uid
        print('[General Scan] Done!')
