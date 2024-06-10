from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create a Quantum Circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to the qubit
qc.h(0)
# Use the Aer simulator to get the statevector
backend = Aer.get_backend('statevector_simulator')
transpiled_circuit = transpile(qc, backend)
result = backend.run(transpiled_circuit).result()

# Get the statevector
state = result.get_statevector()

# Visualize the state on the Bloch sphere
plot_bloch_multivector(state)
plt.title("State after applying Hadamard Gate")
plt.show()
