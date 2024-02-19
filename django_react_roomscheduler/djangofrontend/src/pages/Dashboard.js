import React, {useEffect, useState} from "react";
import Sidebar, {SidebarItem} from '../components/Sidebar';
import TableTiles from './TableTiles'

import {BarChart3, Calendar, FileUp, LayoutDashboard, Settings, UserIcon} from "lucide-react";
export default function Dashboard() {

    const [selectedItem, setSelectedItem] = useState("dashboard");

    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login'
        }
    }, []);

    // Function to handle sidebar item click
    function handleSidebarItemClick(item) {
        setSelectedItem(item);
    }

    return (
        <div className="d-flex bg-gray-100">
            <Sidebar className="sm:w-2/5">
                <SidebarItem icon={<LayoutDashboard size={20}/>} text="Dashboard"
                             onClick={() => handleSidebarItemClick("dashboard")}/>
                <SidebarItem icon={<BarChart3 size={20}/>} text="Insights"
                             onClick={() => handleSidebarItemClick("insights")}/>
                <SidebarItem icon={<Calendar size={20}/>} text="Saved Schedules"
                             onClick={() => handleSidebarItemClick("schedules")}/>
                <SidebarItem icon={<FileUp size={20}/>} text="Import" onClick={() => handleSidebarItemClick("import")}/>
                <hr className='my-3'/>
                <SidebarItem icon={<UserIcon size={20}/>} text="Profile"
                             onClick={() => handleSidebarItemClick("profile")}/>
                <SidebarItem icon={<Settings size={20}/>} text="Settings"
                             onClick={() => handleSidebarItemClick("settings")}/>
            </Sidebar>
            <div className="sm:w-full mt-4 p-4 bg-gray-100 rounded-lg shadow-md">
                {selectedItem === "dashboard" && (
                    <TableTiles/>
                )}
                {selectedItem === "insights" && (
                    <p>Insights</p>
                )}
                {selectedItem === "schedules" && (
                    <p>Saved Schedules</p>
                )}
                {selectedItem === "import" && (
                    <p>Import</p>
                )}
                {selectedItem === "profile" && (
                    <p>Profile</p>
                )}
                {selectedItem === "settings" && (
                    <p>Settings</p>
                )}
            </div>
        </div>
    );
}
