import React, { useState, useEffect } from "react";
import API from "../../services/api";

function InteractionForm() {
  const [formData, setFormData] = useState({
    doctor_name: "",
    hospital: "",
    speciality: "",
    interaction_type: "",
    discussion: "",
    products: "",
    next_followup: "",
  });

  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    const handleEdit = (e) => {
      const item = e.detail;

      setEditingId(item.id);

      setFormData({
        doctor_name: item.doctor_name || "",
        hospital: item.hospital || "",
        speciality: item.speciality || "",
        interaction_type: item.interaction_type || "",
        discussion: item.discussion || "",
        products: item.products || "",
        next_followup: item.next_followup || "",
      });
    };

    window.addEventListener("editInteraction", handleEdit);

    return () => {
      window.removeEventListener("editInteraction", handleEdit);
    };
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const clearForm = () => {
    setEditingId(null);

    setFormData({
      doctor_name: "",
      hospital: "",
      speciality: "",
      interaction_type: "",
      discussion: "",
      products: "",
      next_followup: "",
    });
  };

  const handleSubmit = async () => {

  const payload = {
    ...formData,
    next_followup:
      formData.next_followup === ""
        ? null
        : formData.next_followup,
  };

  console.log("Sending:", payload);

  try {

    if (editingId) {

      await API.put(`/interactions/${editingId}`, payload);

      alert("Interaction Updated Successfully!");

    } else {

      await API.post("/interactions/", payload);

      alert("Interaction Saved Successfully!");

    }

    clearForm();

    window.dispatchEvent(new Event("refreshInteractions"));

  } catch (error) {

    console.log(JSON.stringify(error.response?.data, null, 2));

    alert("Error Saving Interaction");

  }

};
  return (
    <div className="card shadow-sm border-0">
      <div className="card-header bg-white">
        <h4 className="mb-0">
          {editingId ? "Edit Interaction" : "Log HCP Interaction"}
        </h4>
      </div>

      <div className="card-body">

        {/* Row 1 */}
        <div className="row">

          <div className="col-md-6 mb-3">
            <label className="form-label fw-semibold">
              HCP Name
            </label>

            <input
              type="text"
              className="form-control"
              name="doctor_name"
              placeholder="Doctor Name"
              value={formData.doctor_name}
              onChange={handleChange}
            />
          </div>

          <div className="col-md-6 mb-3">
            <label className="form-label fw-semibold">
              Interaction Type
            </label>

            <select
              className="form-select"
              name="interaction_type"
              value={formData.interaction_type}
              onChange={handleChange}
            >
              <option value="">Select</option>
              <option value="Meeting">Meeting</option>
              <option value="Visit">Visit</option>
              <option value="Call">Call</option>
              <option value="Email">Email</option>
            </select>
          </div>

        </div>

        {/* Row 2 */}
        <div className="row">

          <div className="col-md-6 mb-3">
            <label className="form-label fw-semibold">
              Hospital
            </label>

            <input
              type="text"
              className="form-control"
              name="hospital"
              placeholder="Apollo Hospital"
              value={formData.hospital}
              onChange={handleChange}
            />
          </div>

          <div className="col-md-6 mb-3">
            <label className="form-label fw-semibold">
              Speciality
            </label>

            <select
              className="form-select"
              name="speciality"
              value={formData.speciality}
              onChange={handleChange}
            >
              <option value="">Select</option>
              <option value="Cardiology">Cardiology</option>
              <option value="Neurology">Neurology</option>
              <option value="Orthopedics">Orthopedics</option>
              <option value="General Medicine">General Medicine</option>
              <option value="Dermatology">Dermatology</option>
            </select>
          </div>

        </div>

        {/* Discussion */}
        <div className="mb-3">
          <label className="form-label fw-semibold">
            Discussion
          </label>

          <textarea
            rows="4"
            className="form-control"
            name="discussion"
            placeholder="Enter discussion..."
            value={formData.discussion}
            onChange={handleChange}
          />
        </div>

        {/* Products */}
        <div className="mb-3">
          <label className="form-label fw-semibold">
            Products Discussed
          </label>

          <input
            type="text"
            className="form-control"
            name="products"
            placeholder="CardioPlus"
            value={formData.products}
            onChange={handleChange}
          />
        </div>

        {/* Followup */}
        <div className="mb-4">
          <label className="form-label fw-semibold">
            Next Follow-up Date
          </label>

          <input
            type="date"
            className="form-control"
            name="next_followup"
            value={formData.next_followup}
            onChange={handleChange}
          />
        </div>

        <div className="d-flex gap-2">

          <button
            className="btn btn-success w-100"
            onClick={handleSubmit}
          >
            {editingId
              ? "Update Interaction"
              : "Save Interaction"}
          </button>

          {editingId && (
            <button
              className="btn btn-secondary"
              onClick={clearForm}
            >
              Cancel
            </button>
          )}

        </div>

      </div>
    </div>
  );
}

export default InteractionForm;