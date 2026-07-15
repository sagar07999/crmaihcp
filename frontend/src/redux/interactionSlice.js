import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
    name: "interaction",
    initialState: {
        interactions: [],
    },
    reducers: {},
});

export default interactionSlice.reducer;