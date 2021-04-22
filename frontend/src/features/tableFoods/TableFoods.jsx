import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Table } from "react-bootstrap";
import { fetchFoods } from "./tablefoodsSlice";
import TrFood from "./trFood";

function TableFoods({ match }) {
    const dispatch = useDispatch();
    const { foods, isLoading } = useSelector((state) => state.foods);

    useEffect(() => {
        dispatch(fetchFoods(match.path));
    }, [dispatch, match]);

    return (
        <Table striped bordered hover>
            <thead className="thead-light header">
                <tr>
                    <th scope="col" className="header">
                        Nome
                    </th>
                    <th scope="col" className="header">
                        Quantidade
                    </th>
                    <th scope="col" className="header">
                        Proteínas
                    </th>
                    <th scope="col" className="header">
                        Carboidratos
                    </th>
                    <th scope="col" className="header">
                        Gorduras
                    </th>
                </tr>
            </thead>
            {!isLoading ? (
                <tbody>
                    {foods.map((food) => (
                        <TrFood food={food} key={food.id} />
                    ))}
                </tbody>
            ) : (
                <div>Loading...</div>
            )}
        </Table>
    );
}

export default TableFoods;
