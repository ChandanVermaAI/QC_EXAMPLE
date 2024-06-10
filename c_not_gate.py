
# Create a Quantum Circuit with one qubit
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
backend = Aer.get_backend('statevector_simulator')
# Create a Quantum Circuit with two qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to the first qubit to create superposition
qc.h(0)

# Apply CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Use the Aer simulator to get the statevector
result = backend.run(transpile(qc, backend)).result()

# Get the statevector
state = result.get_statevector()

# Visualize the state on the Bloch sphere
plot_bloch_multivector(state)
plt.title("State after applying CNOT Gate")
plt.show()
