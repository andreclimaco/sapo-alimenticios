import { createSlice } from "@reduxjs/toolkit";
import { api } from "./tableFoodsAPI";

const initialState = {
    foods: [],
    isLoading: false,
    error: false,
};

// Slice

const tablefoodsSlice = createSlice({
    name: "foods",
    initialState,
    reducers: {
        startLoading: (state) => {
            state.isLoading = true;
        },
        hasError: (state, action) => {
            state.error = action.payload;
            state.isLoading = false;
        },
        foodsSuccess: (state, action) => {
            state.foods = action.payload;
            state.isLoading = false;
        },
    },
});

export default tablefoodsSlice.reducer;

// Actions

export const { foodsSuccess, startLoading, hasError } = tablefoodsSlice.actions;

export const fetchFoods = (navPath) => async (dispatch) => {
    dispatch(startLoading);
    try {
        await api(navPath).then((response) =>
            dispatch(foodsSuccess(response.data))
        );
    } catch (e) {
        dispatch(hasError(e.message));
        return console.error(e.message);
    }
};
