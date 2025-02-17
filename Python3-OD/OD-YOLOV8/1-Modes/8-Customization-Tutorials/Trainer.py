from ultralytics.models.yolo import DetectionPredictor, DetectionTrainer, DetectionValidator

# YOLO 模型类是训练器类的高级封装。每个YOLO 任务都有自己的训练器，训练器继承自 BaseTrainer.
# 您可以轻松定制培训师，以支持自定义任务或探索研发思路。
# 了解有关定制的更多信息 Trainers, Validators 和 Predictors 以满足您在定制部分的项目需求。

# trainer
trainer = DetectionTrainer(overrides={})
trainer.train()
trained_model = trainer.best

# Validator
val = DetectionValidator(args=...)
val(model=trained_model)

# predictor
pred = DetectionPredictor(overrides={})
pred(source=SOURCE, model=trained_model)

# resume from last weight
overrides["resume"] = trainer.last
trainer = detect.DetectionTrainer(overrides=overrides)

