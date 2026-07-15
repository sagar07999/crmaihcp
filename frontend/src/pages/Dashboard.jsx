import DashboardLayout from "../components/layout/DashboardLayout";
import InteractionList from "../components/interaction/InteractionList";

function Dashboard() {
  return (
    <>
      <DashboardLayout />
      <div className="container-fluid mt-4">
        <InteractionList />
      </div>
    </>
  );
}

export default Dashboard;