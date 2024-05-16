// 코드 틀 https://ant.design/components/menu#menu-demo-horizontal
// AntD 아이콘 https://ant.design/components/icon
import React, { useState } from "react";
import { AppstoreAddOutlined, PlusOutlined } from "@ant-design/icons";
import type { MenuProps } from "antd";
import { Menu } from "antd";
import styled from "styled-components";
// import { Link } from "react-router-dom";

type MenuItem = Required<MenuProps>["items"][number];

const items: MenuItem[] = [
  {
    // label: <Link to="/grid_crud">영화 목록</Link>,
    label: "영화 목록", // 보여지는 이름
    key: "gridCRUD", // Unique ID of the menu item
    icon: <AppstoreAddOutlined />,
  },
  {
    label: "세부 메뉴 있는 경우",
    key: "SubMenu",
    icon: <PlusOutlined />,
    children: [
      {
        type: "group",
        label: "Item 1",
        children: [
          { label: "Option 1", key: "setting:1" },
          { label: "Option 2", key: "setting:2" },
        ],
      },
      {
        type: "group",
        label: "Item 2",
        children: [
          { label: "Option 3", key: "setting:3" },
          { label: "Option 4", key: "setting:4" },
        ],
      },
    ],
  },
];

// AntD + styled-components
const StyledMenu = styled(Menu)`
  background-color: #d2e5ff;
  & > .ant-menu-item,
  .ant-menu-submenu {
    /* display: flex; */
    /* justify-content: center; */
    min-width: 130px;
  }
  /* &.ant-menu-item-selected {
    font-weight: bold;
  } */
`;

const App: React.FC = () => {
  const [current, setCurrent] = useState("gridCRUD"); // 클릭되어 있는 메뉴

  const onClick: MenuProps["onClick"] = (e) => {
    console.log("click ", e);
    setCurrent(e.key);
  };

  return (
    <StyledMenu
      onClick={onClick}
      selectedKeys={[current]}
      mode="horizontal"
      items={items}
    />
  );
};

export default App;
