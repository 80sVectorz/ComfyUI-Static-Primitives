import { app } from "../../../scripts/app.js";
import { addValueControlWidget } from "../../../scripts/widgets.js";

app.registerExtension({
	name: "StaticPrimitives.NumericPrimitives.control_after_generate",
	async nodeCreated(node) { 
        const staticPrimitiveWidgetIndex = node.widgets?.findIndex((w) => w.name === 'Input_FLOAT' || w.name == 'Input_INT'); 
        if (staticPrimitiveWidgetIndex > -1) {
            const staticPrimitiveWidget = node.widgets[staticPrimitiveWidgetIndex];
            const staticPrimitiveValueControl = addValueControlWidget(node, staticPrimitiveWidget, "fixed", null, null, [null,null]); // disgusting fix
            node.widgets.splice(staticPrimitiveWidgetIndex+1,0,node.widgets.pop());
        }
    }
});
app.registerExtension({
	name: "StaticPrimitives.CollectionPrimitives.OutputLabels",
    async beforeRegisterNodeDef(nodeType, nodeData, app){
        if (nodeData.name.endsWith("StaticCollectionPrimitive")){
            const originalNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                originalNodeCreated?.apply(this,arguments);
                var name = this.type;
                name = name.slice(0,name.length-"StaticCollectionPrimitive".length);
                this.addOutput(name,"COMBO");
                this.removeOutput(0);
                originalNodeCreated?.apply(this,arguments);
            }
        }
    }
});