import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
const API_URL = "http://127.0.0.1:8000/tasks";

function Dashboard() {

     const [tasks, setTasks] = useState([]);
    const [binTasks, setBinTasks] = useState([]);
    const [showBin, setShowBin] = useState(false);

    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [status, setStatus] = useState("Pending");

    const [priority, setPriority] = useState("Medium");
    const [filterPriority, setFilterPriority] = useState("All");

    const [editingId, setEditingId] = useState(null);

    const fetchTasks = async () => {
        try {
            const res = await axios.get(`${API_URL}/`);
            setTasks(res.data);
        } catch (error) {
            console.error(error);
        }
    };

    const fetchBinTasks = async () => {
        try {
            const res = await axios.get(`${API_URL}/bin`);
            setBinTasks(res.data);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchTasks();
        fetchBinTasks();
    }, []);
    const addTask = async () => {
        if (!title || !description) {
            alert("Please fill all fields");
            return;
        }

        try {
            await axios.post(`${API_URL}/`, {
                title,
                description,
                status,
                priority,
            });

            setTitle("");
            setDescription("");
            setStatus("Pending");
            setPriority("Medium");

            fetchTasks();
        } catch (error) {
            console.error(error);
        }

    };
    const updateTask = async () => {
        try {
            await axios.put(`${API_URL}/${editingId}`, {
                title,
                description,
                status,
                priority,
            });

            setEditingId(null);
            setTitle("");
            setDescription("");
            setStatus("Pending");
            setPriority("Medium");

            fetchTasks();
        } catch (error) {
            console.error(error);
        }
    };
    const editTask = (task) => {
        setEditingId(task.id);
        setTitle(task.title);
        setDescription(task.description);
        setStatus(task.status);
        setPriority(task.priority);
    };

    const deleteTask = async (id) => {
        try {
            await axios.delete(`${API_URL}/${id}`);

            fetchTasks();
            fetchBinTasks();
        } catch (error) {
            console.error(error);
        }
    };

    const restoreTask = async (id) => {
        try {
            await axios.put(`${API_URL}/restore/${id}`);

            fetchTasks();
            fetchBinTasks();
        } catch (error) {
            console.error(error);
        }
    };

    const permanentDeleteTask = async (id) => {
        try {
            await axios.delete(`${API_URL}/permanent/${id}`);

            fetchBinTasks();
        } catch (error) {
            console.error(error);
        }
    };

    const filteredTasks =
        filterPriority === "All"
            ? tasks
            : tasks.filter(
                (task) => task.priority === filterPriority
            );

    return (
        <div className="container">
            <h1>Website Todo</h1>

            <div className="form-container">
                <input
                    className="input"
                    type="text"
                    placeholder="Task Title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />

                <input
                    className="input"
                    type="text"
                    placeholder="Task Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />

                <select
                    className="input"
                    value={status}
                    onChange={(e) => setStatus(e.target.value)}
                >
                    <option value="Pending">Pending</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                </select>

                <select
                    className="input"
                    value={priority}
                    onChange={(e) => setPriority(e.target.value)}
                >
                    <option value="High">High</option>
                    <option value="Medium">Medium</option>
                    <option value="Low">Low</option>
                </select>
                {editingId ? (
                    <button className="btn" onClick={updateTask}>
                        Update Task
                    </button>
                ) : (
                    <button className="btn" onClick={addTask}>
                        + New Task
                    </button>
                )}
            </div>

            <div className="tabs">
                <button
                    className={!showBin ? "active-tab" : ""}
                    onClick={() => setShowBin(false)}
                >
                    Tasks
                </button>

                <button
                    className={showBin ? "active-tab" : ""}
                    onClick={() => setShowBin(true)}
                >
                    Bin
                </button>
            </div>
            {/* <select
  className="input"
  value={filterPriority}
  onChange={(e) => setFilterPriority(e.target.value)}
>
  <option value="All">All Priorities</option>
  <option value="High">High</option>
  <option value="Medium">Medium</option>
  <option value="Low">Low</option>
</select> */}

            {!showBin ? (
                filteredTasks.map((task) => (
                    <div key={task.id} className="task-card">
                        <h2>{task.title}</h2>
                        <p>{task.description}</p>
                        <p><strong>Priority:</strong> {task.priority}</p>

                        <div
                            className={`status ${task.status
                                .replace(" ", "-")
                                .toLowerCase()}`}
                        >
                            {task.status}
                        </div>

                        <div className="actions">
                            <button
                                className="edit-btn"
                                onClick={() => editTask(task)}
                            >
                                Edit
                            </button>

                            <button
                                className="delete-btn"
                                onClick={() => deleteTask(task.id)}
                            >
                                Delete
                            </button>
                        </div>
                    </div>
                ))
            ) : (
                binTasks.map((task) => (
                    <div key={task.id} className="task-card">
                        <h2>{task.title}</h2>
                        <p>{task.description}</p>
                        <p><strong>Priority:</strong> {task.priority}</p>

                        <div
                            className={`status ${task.status
                                .replace(" ", "-")
                                .toLowerCase()}`}
                        >
                            {task.status}
                        </div>

                        <div className="actions">
                            <button
                                className="restore-btn"
                                onClick={() => restoreTask(task.id)}
                            >
                                Restore
                            </button>

                            <button
                                className="permanent-delete-btn"
                                onClick={() => permanentDeleteTask(task.id)}
                            >
                                Delete Forever
                            </button>
                        </div>
                    </div>
                ))
            )}
        </div>
    );
}

export default Dashboard;