import configureStore from "redux-mock-store";
import thunk from "redux-thunk";
import { api } from "./tableFoodsAPI";

const middlewares = [thunk];
const mockStore = configureStore(middlewares);

function success() {
    return {
        type: "FETCH_DATA_SUCCESS",
    };
}

function fetchData() {
    return (dispatch) => {
        return api("/home").then(() => dispatch(success()));
    };
}

it("should execute fetch data", () => {
    const store = mockStore({});

    // Return the promise
    return store.dispatch(fetchData()).then(() => {
        const actions = store.getActions();
        expect(actions[0]).toEqual(success());
    });
});
