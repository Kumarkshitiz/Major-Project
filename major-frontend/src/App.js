import "./style.css";
import React, { useState } from "react";
import AfterSubmit from "./AfterSubmit";

function App() {
  const [formData, setFormData] = useState({
    age: "",
    tenure: "",
    investmentType: "",
    amount: "",
    riskProfile: "",
  });

  const [errors, setErrors] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false); // State to track if form is submitted

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const validate = () => {
    const newErrors = {};
    if (formData.age < 18 || formData.age > 100) {
      newErrors.age = "Age must be between 18 and 100.";
    }
    if (!formData.investmentType) {
      newErrors.investmentType = "Please select an investment type.";
    }
    if (!formData.amount || formData.amount <= 0) {
      newErrors.amount = "Amount must be greater than 0.";
    }
    if (!formData.riskProfile) {
      newErrors.riskProfile = "Please select a risk profile.";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      console.log("Form submitted successfully!", formData);
      setFormData({
        age: "",
        tenure: "",
        investmentType: "",
        amount: "",
        riskProfile: "",
      });
      setErrors({});
      setIsSubmitted(true); // Redirect to AfterSubmit component
    }
  };

  // Conditionally render AfterSubmit component if form is submitted
  if (isSubmitted) {
    return <AfterSubmit />;
  }

  return (
    <div className="container">
      <h2>Welcome To Smart Financial Advisor</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Age:</label>
          <input
            type="number"
            name="age"
            value={formData.age}
            onChange={handleChange}
          />
          {errors.age && <p className="error">{errors.age}</p>}
        </div>

        <div>
          <label>Tenure (In Years):</label>
          <input
            type="number"
            name="tenure"
            value={formData.tenure}
            onChange={handleChange}
          />
        </div>

        <div>
          <label>Investment Type:</label>
          <div className="radio-group">
            <div>
              <input
                type="radio"
                name="investmentType"
                value="Lumpsum"
                checked={formData.investmentType === "Lumpsum"}
                onChange={handleChange}
              />
              <label>Lumpsum</label>
            </div>
            <div>
              <input
                type="radio"
                name="investmentType"
                value="Monthly"
                checked={formData.investmentType === "Monthly"}
                onChange={handleChange}
              />
              <label>Monthly</label>
            </div>
          </div>
          {errors.investmentType && (
            <p className="error">{errors.investmentType}</p>
          )}
        </div>

        <div>
          <label>Amount:</label>
          <input
            type="number"
            name="amount"
            value={formData.amount}
            onChange={handleChange}
          />
          {errors.amount && <p className="error">{errors.amount}</p>}
        </div>

        <div>
          <label>Risk Profile:</label>
          <select
            name="riskProfile"
            value={formData.riskProfile}
            onChange={handleChange}
          >
            <option value="">Select</option>
            <option value="High">High</option>
            <option value="Moderate">Moderate</option>
            <option value="Low">Low</option>
          </select>
          {errors.riskProfile && (
            <p className="error">{errors.riskProfile}</p>
          )}
        </div>

        <div>
          <button type="submit">Generate Report</button>
        </div>
      </form>
    </div>
  );
}

export default App;
