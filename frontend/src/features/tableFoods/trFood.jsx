const TrFood = ({
    food: { name, quantity, proteins, carbohydrates, fats },
}) => {
    return (
        <tr>
            <td>{name}</td>
            <td>{quantity}g</td>
            <td>{proteins}g</td>
            <td>{carbohydrates}g</td>
            <td>{fats}g</td>
        </tr>
    );
};

export default TrFood;
