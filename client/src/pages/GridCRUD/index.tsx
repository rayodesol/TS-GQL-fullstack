// https://ant.design/components/table#how-to-use
import * as React from "react";
import Navbar from "../../components/Navbar";
import { Table } from "antd";

const dataSource = [
  {
    key: "1",
    name: "Mike",
    age: 32,
    address: "10 Downing Street",
  },
  {
    key: "2",
    name: "John",
    age: 42,
    address: "10 Downing Street",
  },
];

const columns = [
  {
    title: "Name",
    dataIndex: "name",
    key: "name",
  },
  {
    title: "Age",
    dataIndex: "age",
    key: "age",
  },
  {
    title: "Address",
    dataIndex: "address",
    key: "address",
  },
];

export default function App() {
  return (
    <div>
      <Navbar />
      <Table dataSource={dataSource} columns={columns} />
    </div>
  );
}
