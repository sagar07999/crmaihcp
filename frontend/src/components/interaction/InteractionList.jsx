import { useEffect, useState } from "react";
import API from "../../services/api";

function InteractionList() {
  const [interactions, setInteractions] = useState([]);

  // Load all interactions
  const loadInteractions = async () => {
    try {
      const res = await API.get("/interactions/");
      setInteractions(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  // Delete interaction
  const deleteInteraction = async (id) => {
    if (!window.confirm("Delete this interaction?")) return;

    try {
      await API.delete(`/interactions/${id}`);

      alert("Interaction Deleted Successfully!");

      loadInteractions();
    } catch (err) {
      console.log(err);
      alert("Error deleting interaction");
    }
  };

  // Edit interaction
  const editInteraction = (item) => {
    window.dispatchEvent(
      new CustomEvent("editInteraction", {
        detail: item,
      })
    );
  };

  useEffect(() => {
    loadInteractions();

    const refresh = () => {
      loadInteractions();
    };

    window.addEventListener("refreshInteractions", refresh);

    return () => {
      window.removeEventListener(
        "refreshInteractions",
        refresh
      );
    };
  }, []);

  return (
    <div className="card shadow-sm mt-4">

      <div className="card-header bg-white">
        <h5 className="mb-0">Recent Interactions</h5>
      </div>

      <div className="card-body">

        <table className="table table-bordered table-hover align-middle">

          <thead className="table-light">
            <tr>
              <th>Doctor</th>
              <th>Hospital</th>
              <th>Speciality</th>
              <th>Interaction</th>
              <th>Products</th>
              <th>Follow Up</th>
              <th>Summary</th>
              <th width="170">Actions</th>
            </tr>
          </thead>

          <tbody>

            {interactions.length === 0 ? (
              <tr>
                <td colSpan="8" className="text-center">
                  No Interactions Found
                </td>
              </tr>
            ) : (
              interactions.map((item) => (
                <tr key={item.id}>

                  <td>{item.doctor_name}</td>

                  <td>{item.hospital}</td>

                  <td>{item.speciality}</td>

                  <td>{item.interaction_type}</td>

                  <td>{item.products}</td>

                  <td>{item.next_followup || "-"}</td>

                  <td>{item.summary}</td>

                  <td>

                    <button
                      className="btn btn-warning btn-sm me-2"
                      onClick={() => editInteraction(item)}
                    >
                      Edit
                    </button>

                    <button
                      className="btn btn-danger btn-sm"
                      onClick={() =>
                        deleteInteraction(item.id)
                      }
                    >
                      Delete
                    </button>

                  </td>

                </tr>
              ))
            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default InteractionList;