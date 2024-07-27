"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const swagger_1 = require("@nestjs/swagger");
const jira_module_1 = require("./jira/jira.module");
const clickup_module_1 = require("./clickup/clickup.module");
const zapier_module_1 = require("./zapier/zapier.module");
const ml_module_1 = require("./ml-ops/ml.module");
const threat_module_1 = require("./threat/threat.module");
const swaggerConfig = new swagger_1.DocumentBuilder()
    .setTitle('Cyber Threat Intelligence API')
    .setDescription('API for managing cyber threats and automation')
    .setVersion('1.0')
    .addTag('Jira')
    .addTag('ClickUp')
    .addTag('Zapier')
    .addTag('Machine Learning')
    .addTag('Threat Intelligence')
    .build();
const swaggerDocumentOptions = {
    include: [
        jira_module_1.JiraModule,
        clickup_module_1.ClickUpModule,
        zapier_module_1.ZapierModule,
        ml_module_1.MlModule,
        threat_module_1.ThreatModule
    ],
    extraModels: [
        CreateJiraTaskDto,
        UpdateJiraTaskDto,
        CreateClickUpGoalDto,
        UpdateClickUpGoalDto,
        MlAnalysisDto,
        ThreatReportDto
    ],
    ignoreGlobalPrefix: false,
    deepScanRoutes: true,
    operationIdFactory: (controllerKey, methodKey) => `${controllerKey}_${methodKey}`,
};
async function bootstrap() {
    const app = await NestFactory.create(AppModule);
    const document = swagger_1.SwaggerModule.createDocument(app, swaggerConfig, swaggerDocumentOptions);
    swagger_1.SwaggerModule.setup('api', app, document);
    await app.listen(3000);
}
bootstrap();
//# sourceMappingURL=SwaggerDocumentOptions.js.map