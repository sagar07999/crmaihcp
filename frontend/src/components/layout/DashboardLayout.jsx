import Header from "./Header";
import InteractionForm from "../interaction/InteractionForm";
import ChatPanel from "../chat/ChatPanel";
import InteractionList from "../interaction/InteractionList";

function DashboardLayout() {
  return (
    <div className="container-fluid py-4">

      <Header />

      {/* Top Section */}
      <div className="row">

        <div className="col-lg-8 mb-4">
          <InteractionForm />
        </div>

        <div className="col-lg-4 mb-4">
          <ChatPanel />
        </div>

      </div>

      {/* Bottom Section */}
      <div className="row">

        <div className="col-12">
          <InteractionList />
        </div>

      </div>

    </div>
  );
}

export default DashboardLayout;