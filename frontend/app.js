const API_URL = "http://127.0.0.1:5000/transactions";
const form = document.getElementById("transaction-form");
const tableBody = document.querySelector("#transaction-table tbody");

// Load all transactions when page opens
async function loadTransactions() {
  const res = await fetch(API_URL);
  const data = await res.json();
  tableBody.innerHTML = "";
  data.forEach((t) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${t.name}</td>
      <td>$${t.amount.toFixed(2)}</td>
      <td>${t.category}</td>
      <td>${t.date}</td>
      <td>
        <button class="action-btn edit-btn" onclick="editTransaction(${t.id})">Edit</button>
        <button class="action-btn delete-btn" onclick="deleteTransaction(${t.id})">Delete</button>
      </td>
    `;
    tableBody.appendChild(row);
  });
}

// Add new transaction
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    name: document.getElementById("name").value,
    amount: parseFloat(document.getElementById("amount").value),
    category: document.getElementById("category").value,
    date: document.getElementById("date").value,
  };

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  form.reset();
  loadTransactions();
});

// Delete transaction
async function deleteTransaction(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  loadTransactions();
}

// Edit transaction (simple prompt version)
async function editTransaction(id) {
  const name = prompt("Enter new name:");
  const amount = parseFloat(prompt("Enter new amount:"));
  const category = prompt("Enter new category:");
  const date = prompt("Enter new date (YYYY-MM-DD):");

  const data = { name, amount, category, date };

  await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  loadTransactions();
}

// Initialize
loadTransactions();