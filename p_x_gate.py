# Create a Quantum Circuit with one qubit
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
qc = QuantumCircuit(1)
backend = Aer.get_backend('statevector_simulator')

# Apply Pauli-X gate to the qubit
qc.x(0)

# Use the Aer simulator to get the statevector
result = backend.run(transpile(qc, backend)).result()

# Get the statevector
state = result.get_statevector()

# Visualize the state on the Bloch sphere
plot_bloch_multivector(state)
plt.title("State after applying Pauli-X Gate")
plt.show()
