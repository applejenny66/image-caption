#nengo_test.py

import matplotlib.pyplot as plt
#%matplotlib inline

import nengo
import nengo_spa as spa

# Number of dimensions for the Semantic Pointers
dimensions = 32

model = spa.Network(label="Simple question answering")

def color_input(t):
    if (t // 0.5) % 2 == 0:
        return 'RED'
    else:
        return 'BLUE'

def shape_input(t):
    if (t // 0.5) % 2 == 0:
        return 'CIRCLE'
    else:
        return 'SQUARE'

def cue_input(t):
    sequence = ['0', 'CIRCLE', 'RED', '0', 'SQUARE', 'BLUE']
    idx = int((t // (1. / len(sequence))) % len(sequence))
    return sequence[idx]

with model:
    color_in = spa.Transcode(color_input, output_vocab=dimensions)
    shape_in = spa.Transcode(shape_input, output_vocab=dimensions)
    cue = spa.Transcode(cue_input, output_vocab=dimensions)




with model:
    conv = spa.State(dimensions)
    out = spa.State(dimensions)

    # Connect the buffers
    color_in * shape_in >> conv
    conv * ~cue >> out

with model:
    model.config[nengo.Probe].synapse = nengo.Lowpass(0.03)
    p_color_in = nengo.Probe(color_in.output)
    p_shape_in = nengo.Probe(shape_in.output)
    p_cue = nengo.Probe(cue.output)
    p_conv = nengo.Probe(conv.output)
    p_out = nengo.Probe(out.output)

with nengo.Simulator(model) as sim:
    sim.run(3.)   


plt.figure(figsize=(10, 10))
vocab = model.vocabs[dimensions]

plt.subplot(5, 1, 1)
plt.plot(sim.trange(), spa.similarity(sim.data[p_color_in], vocab))
plt.legend(vocab.keys(), fontsize='x-small')
plt.ylabel("color")

plt.subplot(5, 1, 2)
plt.plot(sim.trange(), spa.similarity(sim.data[p_shape_in], vocab))
plt.legend(vocab.keys(), fontsize='x-small')
plt.ylabel("shape")

plt.subplot(5, 1, 3)
plt.plot(sim.trange(), spa.similarity(sim.data[p_cue], vocab))
plt.legend(vocab.keys(), fontsize='x-small')
plt.ylabel("cue")

plt.subplot(5, 1, 4)
for pointer in ['RED * CIRCLE', 'BLUE * SQUARE']:
    plt.plot(sim.trange(), vocab.parse(pointer).dot(sim.data[p_conv].T), label=pointer)
plt.legend(fontsize='x-small')
plt.ylabel("convolved")

plt.subplot(5, 1, 5)
plt.plot(sim.trange(), spa.similarity(sim.data[p_out], vocab))
plt.legend(vocab.keys(), fontsize='x-small')
plt.ylabel("output")
plt.xlabel("time [s]")