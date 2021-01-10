#ifndef DATAVISUALIZATION_H
#define DATAVISUALIZATION_H

#include <QObject>
#include <QtCharts>

class DataVisualization : public QObject
{
    Q_OBJECT
public:
    DataVisualization();
    QChart* get_charts();

private:
    void update_outdoor_datas();
    void update_indoor_datas();
    QMap<QDateTime, QMap<QString, QVariant>> get_data_by_sensor_id(const QString& sensorId);

private:
    QMap<QDateTime, QMap<QString, QVariant>> outdoorDatas;
    QMap<QDateTime, QMap<QString, QVariant>> indoorDatas;
};

#endif  // DATAVISUALIZATION_H