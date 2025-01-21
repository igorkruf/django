```
const data = [
    { name: 'Иван', age: 25, city: 'Москва' },
    { name: 'Мария', age: 30, city: 'Санкт-Петербург' },
    { name: 'Алексей', age: 22, city: 'Казань' },
];

const tableBody = document.querySelector('#myTable tbody');
tableBody.innerHTML = ''; // Очистка содержимого

data.forEach(item => {
    const rowHTML = `
        <tr>
            <td>${item.name}</td>
            <td>${item.age}</td>
            <td>${item.city}</td>
        </tr>
    `;
    tableBody.insertAdjacentHTML('beforeend', rowHTML);
});
```
