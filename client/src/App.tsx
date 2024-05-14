import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import GridCRUD from "./pages/GridCRUD";

const App: React.FC = () => (
  <BrowserRouter>
    <Routes>
      {/* 이후에 path="/grid_crud" 로 변경 예정 */}
      <Route path="/" element={<GridCRUD />} />
    </Routes>
  </BrowserRouter>
);

export default App;
