import { app } from "../../../scripts/app.js";
import { addValueControlWidget } from "../../../scripts/widgets.js";

app.registerExtension({
	name: "StaticPrimitives",
	async nodeCreated(node) { 
        const staticPrimitiveWidgetIndex = node.widgets?.findIndex((w) => w.name === 'Input_FLOAT' || w.name == 'Input_INT'); 
        if (staticPrimitiveWidgetIndex > -1) {
            const staticPrimitiveWidget = node.widgets[staticPrimitiveWidgetIndex];
            const staticPrimitiveValueControl = addValueControlWidget(node, staticPrimitiveWidget, "fixed");
            node.widgets.splice(staticPrimitiveWidgetIndex+1,0,node.widgets.pop());
        }
    }
});